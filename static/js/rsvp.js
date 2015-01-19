// Enable jQuery.wizard for the RSVP page
jQuery(function($) {
    $("#progressbar").progressbar();
    $("#rsvp-form").wizard({
        animations: {
            show: {
                options: {
                    duration: 500
                },
                properties: {
                    opacity: "show"
                }
            },
            hide: {
                options: {
                    duration: 0
                },
                properties: {
                    opacity: "hide"
                }
            }
        },
        afterSelect: function(event, state) {
            $("#progressbar").progressbar("value", state.percentComplete);
            $("#location").text("(" + state.stepsComplete + "/" + state.stepsPossible + ")");
        },
	transitions: {
            married: function(state, action) {
                if (state.step.find("#coming-2").is(':checked')) {
                    return "other-comments";
                } else if (state.step.find("#married-1").is(':checked')) {
                    return "married";
                } else {
                    return "not-married";
                }
            },
            affection: function(state, action) {
                if ($("input[name=partner]").val() == '') {
                    return "mcq";
                } else {
                    return "partner-affection";
                }
            }
	}
    }).validate({
    });
});
