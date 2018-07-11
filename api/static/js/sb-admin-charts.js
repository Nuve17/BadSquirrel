// Chart.js scripts
// -- Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';
// -- Area Chart Example
var result = [{ x: "18:00", y: "230" }, { x: "19:00", y: "232" }, { x: "20:00", y: "236" }, { x: "22:00", y: "228" }];

// parse labels and data
var labels = result.map(e => moment(e.x, 'HH:mm'));
var data = result.map(e => +e.y);
var ctx = document.getElementById("myAreaChart");
var myLineChart = new Chart(ctx, {
   type: 'line',
   data: {
      labels: labels,
      datasets: [{
         label: 'Voltage Fluctuation',
         data: data,
         borderWidth: 1
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
         }]
      },
   }
});
// -- Bar Chart Example
var ctx = document.getElementById("myBarChart");
var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ["January", "February", "March", "April", "May", "June"],
    datasets: [{
      label: "Revenue",
      backgroundColor: "rgba(2,117,216,1)",
      borderColor: "rgba(2,117,216,1)",
      data: [4215, 5312, 6251, 7841, 9821, 14984],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'month'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 6
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 15000,
          maxTicksLimit: 5
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
// -- Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["Blue", "Red", "Yellow", "Green"],
    datasets: [{
      data: [12.21, 15.58, 11.25, 8.32],
      backgroundColor: ['#007bff', '#dc3545', '#ffc107', '#28a745'],
    }],
  },
});
