// linear color scale
// interact with this variable from a javascript console
var pc_progressive;

// load csv file and create the chart
d3.csv('data/itg.csv', function(data) {
  var colorgen = d3.scale.category20();
  var colors = {};
  // _(data).chain()
  //   .pluck('group')
  //   .uniq()
  //   .each(function(d,i) {
  //     colors[d] = colorgen(i);
  //   });

  var color = function(d) { return colors[d.group]; };

  pc_progressive = d3.parcoords()("#example-progressive")
    .data(data)
    .color(color)
    .alpha(0.4)
    .margin({ top: 24, left: 150, bottom: 12, right: 0 })
    .mode("queue")
    .render()
    .brushable()  // enable brushing
    .interactive()  // command line mode

  pc_progressive.svg.selectAll("text")
    .style("font", "10px sans-serif");
});
