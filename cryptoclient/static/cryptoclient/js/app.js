$(document).ready(function () {
    $("#id_symmetric_tech").hide();
    $("#id_asymmetric_tech").hide();
    $('.message-key').hide();
    var choice = 'input[type=radio][name=choice]'; // get the value of radio button choice(Symmetric or Assymetric)
    var symmetric_tech = 'input[type=radio][name=symmetric_tech]'; // get the value of radio button symmetric technique for e.g ceaser cipher, hill cipher etc.
    var asymmetric_tech = 'input[type=radio][name=asymmetric_tech]'; // get the value of radio button Asymmetric technique for e.g des 8 etc.
    if ($(choice).is(':checked')) {
        
        
        if ($(choice).val() == "Symmetric Algo") {
            
            $("#id_symmetric_tech").fadeIn();
            $("#id_asymmetric_tech").hide();
            if ($(symmetric_tech).is(':checked')) {
                $(asymmetric_tech).removeAttr('required')
                $(symmetric_tech).attr('required', true)
                $(".message-key").fadeIn();
            }
        }
        else if ($(choice).val() == "ASymmetric Algo") {
            $("#id_symmetric_tech").hide();
            $("#id_asymmetric_tech").fadeIn();
            if ($(asymmetric_tech).is(':checked')) {
                $(symmetric_tech).removeAttr('required')
                $(asymmetric_tech).attr('required', true)
                $(".message-key").fadeIn();
            }
        }

    }

    $(choice).change(function () {
        
        $(".message-key").hide();
        
        if ($(this).val() == "Symmetric Algo") {
            $(asymmetric_tech).removeAttr('required')
            $(symmetric_tech).attr('required', true)
            $("#id_symmetric_tech").fadeIn();
            $("#id_asymmetric_tech").hide();
            if ($(symmetric_tech).is(':checked')) {
                $(".message-key").fadeIn();
            }
            
            $(symmetric_tech).change(function () {
                console.log($(this).val());
                if ($(this).val() == "ceaser cipher") {
                    $(".message-key").fadeIn();

                }
                else if ($(this).val() == "play fair") {
                    $(".message-key").fadeIn();
                }
                else if ($(this).val() == "hill cipher") {
                    $(".message-key").fadeIn();
                }
                else {
                    $(".message-key").hide();

                }
            });
        }
        else {
            $(symmetric_tech).removeAttr('required')
            $(asymmetric_tech).attr('required', true)
            $("#id_symmetric_tech").hide();
            $("#id_asymmetric_tech").fadeIn();
            if ($(asymmetric_tech).is(':checked')) {
                $(".message-key").fadeIn();
            }
            $(asymmetric_tech).change(function () {
                console.log($(this).val())
                if ($(this).val() == "des") {
                    $(".message-key").fadeIn();

                }
                else {
                    $(".message-key").hide();

                }
            });
        }
    });

});

