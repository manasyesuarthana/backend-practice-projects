document.addEventListener('DOMContentLoaded', function() {
    const tabs = document.querySelectorAll('.tab');
    const valueInput = document.getElementById('value');
    const fromUnitSelect = document.getElementById('from_unit');
    const toUnitSelect = document.getElementById('to_unit');
    const convertBtn = document.getElementById('convert-btn');
    const resultDiv = document.getElementById('result');
    
    // Unit options for each category
    const unitOptions = {
        length: [
            {value: 'mm', text: 'Millimeter (mm)'},
            {value: 'cm', text: 'Centimeter (cm)'},
            {value: 'm', text: 'Meter (m)'},
            {value: 'km', text: 'Kilometer (km)'},
            {value: 'in', text: 'Inch (in)'},
            {value: 'ft', text: 'Foot (ft)'},
            {value: 'yd', text: 'Yard (yd)'},
            {value: 'mi', text: 'Mile (mi)'}
        ],
        weight: [
            {value: 'mg', text: 'Milligram (mg)'},
            {value: 'g', text: 'Gram (g)'},
            {value: 'kg', text: 'Kilogram (kg)'},
            {value: 'oz', text: 'Ounce (oz)'},
            {value: 'lb', text: 'Pound (lb)'}
        ],
        temp: [
            {value: 'c', text: 'Celsius (°C)'},
            {value: 'f', text: 'Fahrenheit (°F)'},
            {value: 'k', text: 'Kelvin (K)'}
        ]
    };
    
    let currentUnitType = 'length';
    
    // Initialize with length units
    populateUnitSelects(unitOptions.length);
    
    // Tab switching
    tabs.forEach(tab => {
        tab.addEventListener('click', function() {
            tabs.forEach(t => t.classList.remove('active'));
            this.classList.add('active');
            
            currentUnitType = this.getAttribute('data-type');
            
            // Update unit selects based on selected tab
            if (currentUnitType === 'length') {
                populateUnitSelects(unitOptions.length);
            } else if (currentUnitType === 'weight') {
                populateUnitSelects(unitOptions.weight);
            } else if (currentUnitType === 'temp') {
                populateUnitSelects(unitOptions.temp);
            }
            
            // Clear result
            clearResult();
        });
    });
    
    // Convert button click
    convertBtn.addEventListener('click', function() {
        const value = valueInput.value;
        const fromUnit = fromUnitSelect.value;
        const toUnit = toUnitSelect.value;
        
        if (!value) {
            showError('Please enter a value to convert');
            return;
        }
        
        convertValue(value, fromUnit, toUnit);
    });
    
    function populateUnitSelects(options) {
        // Clear existing options
        fromUnitSelect.innerHTML = '';
        toUnitSelect.innerHTML = '';
        
        // Add new options
        options.forEach(option => {
            const fromOption = document.createElement('option');
            fromOption.value = option.value;
            fromOption.textContent = option.text;
            fromUnitSelect.appendChild(fromOption);
            
            const toOption = document.createElement('option');
            toOption.value = option.value;
            toOption.textContent = option.text;
            toUnitSelect.appendChild(toOption);
        });
        
        // Set different default "to" units for better UX
        if (currentUnitType === 'length') {
            fromUnitSelect.value = 'm';
            toUnitSelect.value = 'ft';
        } else if (currentUnitType === 'weight') {
            fromUnitSelect.value = 'kg';
            toUnitSelect.value = 'lb';
        } else if (currentUnitType === 'temp') {
            fromUnitSelect.value = 'c';
            toUnitSelect.value = 'f';
        }
    }
    
    function convertValue(value, fromUnit, toUnit) {
        // Show loading state
        resultDiv.textContent = 'Converting...';
        resultDiv.className = 'result';
        
        // Send request to our frontend Flask app
        fetch('/convert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                'unit_type': currentUnitType,
                'value': value,
                'from_unit': fromUnit,
                'to_unit': toUnit
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                showError(data.error);
            } else {
                showResult(
                    data.original_value, 
                    data.original_unit, 
                    data.converted_value, 
                    data.converted_unit
                );
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showError('An error occurred during conversion');
        });
    }
    
    function showResult(originalValue, originalUnit, convertedValue, convertedUnit) {
        resultDiv.innerHTML = `
            <strong>${originalValue} ${originalUnit}</strong> = 
            <strong>${convertedValue} ${convertedUnit}</strong>
        `;
        resultDiv.className = 'result success';
    }
    
    function showError(message) {
        resultDiv.textContent = message;
        resultDiv.className = 'result error';
    }
    
    function clearResult() {
        resultDiv.textContent = '';
        resultDiv.className = 'result';
    }
});