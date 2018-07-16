// Chart.js scripts
// -- Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';
// -- Area Chart Example
//var result = [{ x: "18:30", y: "230" }, { x: "19:00", y: "235" }, { x: "19:30", y: "232" },{ x: "20:00", y: "236" },{ x: "20:45", y: "229" }, { x: "22:00", y: "228" }];
console.log("Avant ouverture----------------------------------------------------")
d3.json('./static/json_data/datastat.json', function(json) {

  // parse labels and data
  var result = json
  
  console.log('resultttttttttttttttttttttttt'+typeof(result))
  var labels = result.map(e => moment(e.x, 'HH:mm'));
  var data = result.map(e => +e.y);
  var ctx = document.getElementById("myAreaChart");
  var myLineChart = new Chart(ctx, {
     type: 'line',
     data: {
        labels: labels,
        datasets: [{
           label: 'Traffic clients',
           data: data,
           borderWidth: 1,
                 
      backgroundColor: "rgba(2,117,216,0.2)",
      borderColor: "rgba(2,117,216,1)",
      pointRadius: 5,
      pointBackgroundColor: "rgba(2,117,216,1)",
      pointBorderColor: "rgba(255,255,255,0.8)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(2,117,216,1)",
      pointHitRadius: 20,
      pointBorderWidth: 2
        }]
     },
     options: {
        scales: {
           xAxes: [{
              type: 'time',
              time: {
                 unit: 'hour',
                 displayFormats: {
                    hour: 'HH:mm'
                 }
              }
           }],
           yAxes: [{
        gridLines: {
          color: "rgba(0, 0, 0, .125)",
        }
      }]
        },
     }
  });

});

// -- Pie Chart Example
d3.json('./static/json_data/os.json', function(json) {
object1 = json;
var labelOS = [];
var dataOS = [];
for (var property1 in object1) {
  labelOS.push(property1)
  dataOS.push(object1[property1])
}
console.log(json['ip'])
  var ctx = document.getElementById("myPieChart");
  var myPieChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
      //labels: ["Windows", "Linux", "Autres"],
      labels: labelOS,
      datasets: [{
        //data: [1, 15.58, 51],
        data: dataOS,
        //data: [12.21, 15.58, 11.25, 8.32],
        backgroundColor: ['#007bff', '#dc3545', '#ffc107'],
      }],
    },
  });
});


d3.json('./static/json_data/domainstat.json', function(json) {
  //obj=JSON.parse(json)
  var chart = new CanvasJS.Chart("chartContainer", {
    animationEnabled: true,
    
    title:{
      text:"Les sites les plus visités"
    },
    axisX:{
      interval: 1
    },
    axisY2:{
      interlacedColor: "rgba(1,77,101,.2)",
      gridColor: "rgba(1,77,101,.1)",
      title: "Nombre de visites"
    },
    data: [{
      type: "bar",
      name: "companies",
      axisYType: "secondary",
      color: "#014D65",
      dataPoints: json/*[
        { label: "Sweden",y: 3  },
        {  label: "Taiwan",y: 7 },
        { y: 5, label: "Russia" },
        { y: 9, label: "Spain" },
        { y: 7, label: "Brazil" },
        { y: 7, label: "India" },
        { y: 9, label: "Italy" },
        { y: 8, label: "Australia" },
        { y: 11, label: "Canada" },
        { y: 15, label: "South Korea" },
        { y: 12, label: "Netherlands" },
        { y: 15, label: "Switzerland" },
        { y: 25, label: "Britain" },
        { y: 28, label: "Germany" },
        { y: 29, label: "France" },
        { y: 52, label: "Japan" },
        { y: 103, label: "China" },
        { label: "US",y: 134}
      ]*/
    }]
  });
  chart.render();

});
