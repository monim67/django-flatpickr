"use strict";

(function () {
  if (window.isFlatpickrInitialized) return;
  window.isFlatpickrInitialized = true;
  /**
   * @typedef {object} FlatpickrInstance
   * @property {Date[]} selectedDates
   * @property {boolean} isMobile
   * @property {HTMLInputElement?} mobileInput
   * @property {FlatpickrOptions} config
   *
   * @typedef {object} FlatpickrOptions
   * @property {FlatpickrHookFunction[]} onChange
   *
   * @callback FlatpickrHookFunction
   * @param {Date[]} selectedDates
   * @param {string} dateStr
   * @param {FlatpickrInstance} instance
   *
   * @typedef {object} DjangoFlatpickrConfig
   * @property {string} range_from
   * @property {FlatpickrOptions} options
   */

  /** @type {WeakMap<HTMLInputElement, FlatpickrInstance>} */
  const flatpickrInstances = new WeakMap();
  class DjangoFlatpickrError extends Error {
    /**
     * @param {HTMLInputElement} inputElement
     * @param {string} message
     */
    constructor(inputElement, message) {
      super(`input name: ${inputElement.name}; ${message}`);
      this.name = "django-flatpickr error";
      this.inputElement = inputElement
    }
  }

  /**
   * @param {DjangoFlatpickrError} err
   */
  function handleError(err) {
    if (err.inputElement.hasAttribute('data-debug')) {
      const errDisplay = document.createElement("b");
      errDisplay.innerHTML = "Check browser console for errors, Set django DEBUG=False to hide this error message";
      errDisplay.style.color = "red";
      err.inputElement.after(errDisplay);
    }
    throw err;
  }

  document.addEventListener('DOMContentLoaded', function (event) {
    findAndProcessFlatpickrInputs(document);
    document.addEventListener('DOMNodeInserted', function (event) {
      setTimeout(() => {
        if (event.target.querySelectorAll) findAndProcessFlatpickrInputs(event.target);
      });
    });
  });

  /**
   * @param {HTMLElement} htmlElement
   */
  function findAndProcessFlatpickrInputs(htmlElement) {
    /** @type {NodeListOf<HTMLInputElement>} */
    const inputElements = htmlElement.querySelectorAll('[data-fpconfig]:not([disabled])')
    for (const inputElement of inputElements) {
      try {
        if (typeof flatpickr == 'function') {
          createFlatpickrInstance(inputElement);
        } else {
          throw Error('flatpickr js/css resources was not loaded, please check your CDN links');
        }
      }
      catch (err) {
        handleError(new DjangoFlatpickrError(inputElement, err.message));
      }
    }
  }

  /**
   * @param {HTMLInputElement} inputElement
   */
  function createFlatpickrInstance(inputElement) {
    const config = getConfig(inputElement);
    const inputWrapper = inputElement.closest('.django-flatpickr');
    if (!inputWrapper) throw Error('input must have a parent with class="django-flatpickr"')
    inputElement.setAttribute('data-input', '');
    /** @type {FlatpickrInstance} */
    const flatpickrInstance = flatpickr(inputWrapper, config.options);
    flatpickrInstances.set(inputElement, flatpickrInstance);

    if (config.range_from) {
      const flatpickrRangeFromInstance = getRangeFromInputElement(inputElement, config);
      if (flatpickrRangeFromInstance) {
        configureRangeSelection(flatpickrRangeFromInstance, flatpickrInstance);
      }
    }
  }

  /**
   * @param {HTMLInputElement} inputElement
   */
  function getConfig(inputElement) {
    let /** @type {DjangoFlatpickrConfig} */ config;
    try {
      config = JSON.parse(inputElement.getAttribute('data-fpconfig'));
    }
    catch (err) { throw Error("Invalid config") }
    const optionKeyName = inputElement.name.replace(/^(.*-)?/, "djangoFlatpickrOptions_")
    config.options = { ...window.djangoFlatpickrOptions, ...window[optionKeyName], ...config.options };
    return config;
  }

  /**
   * @param {HTMLInputElement} inputElement
   * @param {DjangoFlatpickrConfig} config
   */
  function getRangeFromInputElement(inputElement, config) {
    const rangeFromInputName = inputElement.name.replace(/[^-]+$/, config.range_from);
    let fromInputElement = inputElement.form?.elements.namedItem(rangeFromInputName);
    if (!fromInputElement) {
      const elements = document.querySelectorAll(`input[name="${config.range_from}"]`);
      if (elements.length == 0) throw Error("range_from not found");
      if (elements.length > 1) throw Error("Multiple range_from found");
      fromInputElement = elements[0];
    }
    if (flatpickrInstances.has(fromInputElement)) {
      return flatpickrInstances.get(fromInputElement);
    } else {
      throw Error(`range_from "${config.range_from}" is not a flatpickr input`);
    }
  }

  /**
   * @param {FlatpickrInstance} fromInstance
   * @param {FlatpickrInstance} toInstance
   */
  function configureRangeSelection(fromInstance, toInstance) {
    registerOnTimeValueChange(fromInstance, function (selectedDates) {
      toInstance.set('minDate', selectedDates[0] || false);
      if (fromInstance.isMobile && toInstance.isMobile) {
        toInstance.mobileInput.min = fromInstance.mobileInput.value;
      }
    });
    registerOnTimeValueChange(toInstance, function (selectedDates) {
      fromInstance.set('maxDate', selectedDates[0] || false);
      if (fromInstance.isMobile && toInstance.isMobile) {
        fromInstance.mobileInput.max = toInstance.mobileInput.value;
      }
    });
  }

  /**
   * Fires onChange event only when there's change in the time value
   * of selectedDate[0], otherwise drops the onChange event
   * @param {FlatpickrInstance} instance
   * @param {FlatpickrHookFunction} hookFunction
   */
  function registerOnTimeValueChange(instance, hookFunction) {
    let oldTimeValue = getTimeValue(instance.selectedDates);
    hookFunction(instance.selectedDates);
    instance.config.onChange.push(function (selectedDates) {
      const newTimeValue = getTimeValue(selectedDates);
      if (newTimeValue !== oldTimeValue) {
        oldTimeValue = newTimeValue;
        hookFunction(selectedDates);
      }
    });
  }

  /**
   * Get time value of selectedDate[0]
   * @param {Date[]} selectedDates
   */
  function getTimeValue(selectedDates) {
    return selectedDates.length ? selectedDates[0].getTime() : 0;
  }
})();
