var tablinks = document.getElementsByClassName("tab-links");
var tabcontents = document.getElementsByClassName("tab-contents");
var openbutton = document.getElementById("bx-menu")

function opentab(tabname){
    var tablink;
    for(tablink of tablinks){
            tablink.classList.remove("active-link")
    }
    var tabcontent;
    for(tabcontent of tabcontents){
        tabcontent.classList.remove("active-tab")
    }
    event.currentTarget.classList.add("active-link");
    document.getElementById(tabname).classList.add("active-tab")
}

function openMenu(){
    sidemenu.style.right= "0";
    openbutton.style.color= "rgba(0,0,0,1)";

}

function closeMenu(){
    sidemenu.style.right= "-200px";
    openbutton.style.color= "white";

}


