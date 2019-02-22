document.addEventListener('DOMContentLoaded', function (event) {
    let flatpickr_db = {}, linked_configs = [];
    document.querySelectorAll('[fp_config]:not([disabled])').forEach(function (inputElement) {
        try {
            var config = JSON.parse(inputElement.getAttribute('fp_config'));
        }
        catch (x) { }
        if (config.id && config.options) {
            let inputWrapper;
            if (config.options.wrap) {
                inputElement.setAttribute('data-input', '');
                inputWrapper = inputElement.closest('.flatpickr-wrapper');
                if (!inputWrapper) {
                    throw new Error(
                        'django-flatpickr error:: When wrap option is set to true, ' +
                        'flatpickr input element should be contained by ".flatpickr-wrapper" element'
                    )
                }
            }
            if (config.linked_to) linked_configs.push(config);
            flatpickr_db[config.id] = {
                config: config,
                instance: flatpickr(inputWrapper || inputElement, config.options)
            }
        }
    });
    linked_configs.forEach(function (config) {
        let flatpickr_from_instance = flatpickr_db[config.linked_to].instance;
        let flatpickr_to_instance = flatpickr_db[config.id].instance;
        flatpickrOnChange(flatpickr_from_instance, function(selectedDates){
            flatpickr_to_instance.set('minDate', selectedDates[0] || false);
        });
        flatpickrOnChange(flatpickr_to_instance, function(selectedDates){
            flatpickr_from_instance.set('maxDate', selectedDates[0] || false);
        });
    });
    function flatpickrOnChange(instance, callbackFn){
        /* This prevents the infinite loop */
        function resolveTime(selectedDates){
            return selectedDates.length ? selectedDates[0].getTime() : 0;
        }
        let rememberedTime = resolveTime(instance.selectedDates);
        callbackFn(instance.selectedDates, true);
        instance.set('onChange', function (selectedDates) {
            let selectedTime = resolveTime(selectedDates);
            if(selectedTime != rememberedTime){
                rememberedTime = selectedTime;
                callbackFn(selectedDates);
            }
        });
    }
});
