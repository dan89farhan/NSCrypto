$(document).ready(function() {
    $('input[type=radio][name=choice]').change(function() {
        if (this.value == 'Symmetric Algo') {
            console.log("Allot Thai Gayo Bhai");
        }
        
        else{
            console.log("Transfer Thai Gayo");
        }
    });
});