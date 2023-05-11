$(function() {
        var i= 1;
        $('#addsummury').live('click', function() {
                $('<p><textarea class="form-control"  name="summury['+i+']" placeholder="Enter Skill Summury"></textarea><a href="#" id="removesummury">Remove</a></p>').appendTo('#skill_summury');
                i++;
                return false;
        });
        
        $('#removesummury').live('click', function() { 
                if( i > 0 ) {
                        $(this).parents('p').remove();
                        i--;
                }
                return false;
        });
});

$(function() {
        var i= 1;
        $('#addacademics').live('click', function() { 
                $('<div><p>Course<input type="text" class="form-control"  name="course['+i+']" placeholder="Enter Course"></p>'+
                '<p>University<select class="form-control"  name="university['+i+']"><option value="">-- select university --</option><option value="VTU">VTU</option><option value="autonomous">autonomus</option></select></p>'+
                '<p>Result<input type="number" class="form-control"  name="result['+i+']"  placeholder="Enter Result"></p>'+
                '<p>Passout Year <select class="form-control"  name="passout['+i+']"> <option value="">-- select year --</option> <option value=1999>1999</option> <option value=2000>2000</option><option value=2001>2001</option><option value=2002>2002</option><option value=2003>2003</option><option value=2004>2004</option><option value=2005>2005</option><option value=2006>2006</option><option value=2007>2007</option><option value=2008>2008</option><option value=2009>2009</option><option value=2010>2010</option><option value=2011>2011</option><option value=2012>2012</option><option value=2013>2013</option><option value=2014>2014</option><option value=2015>2015</option><option value=2016>2016</option><option value=2017>2017</option><option value=2018>2018</option><option value=2019>2019</option><option value=2020>2020</option><option value=2021>2021</option></select></p>');
                i++;
                return false;
        });
        
        $('#removeacademics').live('click', function() { 
                if( i > 0 ) {
                        $(this).parent().parent('div').remove();
                        i--;
                }
                return false;
        });
});

$(function() {
        var i= 1;
        $('#addactivities').live('click', function() { 
                $('<p><textarea class="form-control"  name="activities['+i+']" placeholder="Enter Activity"></textarea><a href="#" id="removeactivities">Remove</a></p>').appendTo('#curricular_activities');
                i++;
                return false;
        });
        
        $('#removeactivities').live('click', function() { 
                if( i > 0 ) {
                        $(this).parents('p').remove();
                        i--;
                }
                return false;
        });
});

$(function() {
        var i= 1;
        $('#addstrength').live('click', function() { 
                $('<p><textarea class="form-control"  name="strength['+i+']" placeholder="Enter Strength"></textarea><a href="#" id="removestrength">Remove</a></p>').appendTo('#strength');
                i++;
                return false;
        });

        $('#removestrength').live('click', function() { 
                if( i > 0 ) {
                        $(this).parents('p').remove();
                        i--;
                }
                return false;
               
        });        
});

let navItems= ['#form1', '#form2', '#form3', '#form4', '#form5', '#form6', '#form7', '#form8', '#form9'];
function handleNavigation(e) {
    var id =(e.target.getAttribute('data-value'))
    var id1 = navItems[navItems.indexOf(id) - 1]
    var a = 0

    $(id1).find(':input').each(function(e){	
        if(this.tagName != 'BUTTON'){
                if (!this.value){
                        this.focus()
                        a = 1
                }
                if(this.id == 'phone_check'){
                        var nm = this.value
                        if(nm.length != 10){
                        alert('Enter 10 digit phone number')
                        }
                }

        }
    });

    if(a==0){
    navItems.map(function(item) {
        if(id === item ) {
            $(item).addClass("active");
        }
        else {
        $(item).removeClass("active");
        }
    
    })
}
}

let Items= ['#ug', '#puc', '#sslc'];
function handleNav(e) {
    var Id =(e.target.getAttribute('data-value'))
    Items.map(function(item) {
        if(Id === item ) {
            $(item).addClass("active");
        }
        else {
        $(item).removeClass("active");
        }
    })
}