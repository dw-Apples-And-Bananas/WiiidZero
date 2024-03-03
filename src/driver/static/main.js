// document.onmousemove = function(e) {
//   var x = e.pageX;
//   var y = e.pageY;
//   e.target.style.setProperty('--x', x + 'px');
//   e.target.style.setProperty('--y', y + 'px');
// };
document.onmousemove = function (event) {
  var x = (event.clientX / window.innerWidth) * 100;
  var y = (event.clientY / window.innerHeight) * 100;
  
  document.body.style.setProperty('--x', x + '%');
  document.body.style.setProperty('--y', y + '%');
}
