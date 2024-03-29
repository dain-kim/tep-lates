// Format date
var today = new Date();
var dd = today.getDate();
var mm = today.getMonth() + 1;
var yyyy = today.getFullYear();
var date = today.getDay();
var dateList = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
document.getElementById("date").innerHTML = mm+'/'+dd+'/'+yyyy+', '+dateList[date]+' &#129425;';

// Expand and collapse tabs
function openTab(evt, tabName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}

// Nested checkboxes
// var veganCheckboxes = document.querySelectorAll('input.vegan-sub');
// var vegetarianCheckboxes = document.querySelectorAll('input.vegetarian-sub');
// var meatCheckboxes = document.querySelectorAll('input.meat-sub');
// veganCheck = document.getElementById('vegan');
// vegetarianCheck = document.getElementById('vegetarian');
// meatCheck = document.getElementById('meat');
// document.getElementById('print').innerHTML += "tablinks length "+tablinks.length;
var checkboxes = document.querySelectorAll('input.meat-sub'),
    checkall = document.getElementById('meat');

for(var i=0; i<checkboxes.length; i++) {
  checkboxes[i].onclick = function() {
    var checkedCount = document.querySelectorAll('input.meat-sub:checked').length;
    checkall.checked = checkedCount > 0;
    checkall.indeterminate = checkedCount > 0 && checkedCount < checkboxes.length;
  }
}

checkall.onclick = function() {
  for(var i=0; i<checkboxes.length; i++) {
    checkboxes[i].checked = this.checked;
  }
}