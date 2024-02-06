document.addEventListener('DOMContentLoaded', function() {
    const selectedCells = JSON.parse(localStorage.getItem('selectedCells') || '[]');
    const rankingForm = document.getElementById('rankingForm');

    // Generate ranking options for each selected cell
    selectedCells.forEach(cellId => {
        const formGroup = document.createElement('div');
        formGroup.className = 'form-group';

        const label = document.createElement('label');
        label.textContent = `Rank for Cell ${cellId}:`;

        const select = document.createElement('select');
        select.className = 'form-control';
        select.name = cellId;

        // Populate select options (1 to 3)
        for (let i = 1; i <= 3; i++) {
            const option = document.createElement('option');
            option.value = i;
            option.textContent = i;
            select.appendChild(option);
        }
        console.log("Selected cells:", selectedCells);
        
        formGroup.appendChild(label);
        formGroup.appendChild(select);
        rankingForm.appendChild(formGroup);
    });

    // Handle form submission
    document.getElementById('submitRankings').addEventListener('click', function(e) {
        e.preventDefault();
        const rankings = {};
        selectedCells.forEach(cellId => {
            const selectElement = document.querySelector(`select[name="${cellId}"]`);
            rankings[cellId] = selectElement.value;
        });

        // Store the rankings in localStorage
        localStorage.setItem('rankings', JSON.stringify(rankings));

        // Redirect to another page to use the rankings
        window.location.href = '/results';  // Make sure you have a Flask route for '/results'
    });
});

