$(document).ready(function() {
    $('input[type=radio][name=choice]').change(function() {
        if($(this).val() == "Symmetric Algo"){
            $("#id_symmetric_tech").fadeIn();
            $("#id_asymmetric_tech").hide();
        }
        else{
            $("#id_symmetric_tech").hide();
            $("#id_asymmetric_tech").fadeIn();
        }
    });
});