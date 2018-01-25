$(document).ready(function () {
    $("#id_symmetric_tech").hide();
    $("#id_asymmetric_tech").hide();
    $('.message-key').hide();
    var choice = 'input[type=radio][name=choice]'; // get the value of radio button choice(Symmetric or Assymetric)
    var symmetric_tech = 'input[type=radio][name=symmetric_tech]'; // get the value of radio button symmetric technique for e.g ceaser cipher, hill cipher etc.
    if ($(choice).is(':checked') &&  $(choice).val() == "Symmetric Algo"){
        $("#id_symmetric_tech").fadeIn();
        $("#id_asymmetric_tech").hide();
        if ($(symmetric_tech).is(':checked') ){
            $(".message-key").fadeIn();
        }
    }
    else if($(choice).is(':checked') &&  $(choice).val() == "ASymmetric Algo"){
        $("#id_symmetric_tech").hide();
        $("#id_asymmetric_tech").fadeIn();
    }
    
    $(choice).change(function () {
        console.log($(choice))
        $(".message-key").hide();
        if ($(this).val() == "Symmetric Algo") {
            $("#id_symmetric_tech").fadeIn();
            $("#id_asymmetric_tech").hide();
            if ($(symmetric_tech).is(':checked') ){
                $(".message-key").fadeIn();
            }
            $(symmetric_tech).change(function () {
                
                if ($(this).val() == "ceaser cipher") {
                    $(".message-key").fadeIn();
                    
                }
                else {
                    $(".message-key").hide();
                    
                }
            });
        }
        else {
            $("#id_symmetric_tech").hide();
            $("#id_asymmetric_tech").fadeIn();
        }
    });

});

