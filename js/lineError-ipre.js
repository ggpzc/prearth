
var chartDom_ipre = document.getElementById('lineError-ipre');
var myChart_ipre = echarts.init(chartDom_ipre);
var option_ipre_template;


var ipre_sub_map;
var colors = ["#D89C7A", "#849B91", "#8A95A9", "#686789", "#B77F70","#88878D"]
// read data from local position'../data/sex_female.json'

fetch("https://ggpzc.github.io/prearth.github.io/data_preprocessed/key_mapping.json")
  .then(response => response.json())
  .then(json => {
    // copy option_template to option
    ipre_sub_map = json;
    console.log(ipre_sub_map);
  });


option_ipre_template = {
  tooltip: {
    // trigger: 'axis',
  },
  title: {
    text: '',
    subtext: '',
    left: 'center',
    textStyle: {
       fontWeight: 'bolder'
       
    }
    
  },
  legend: {
    orient: 'vertical',
    left: 'right',
    align: 'left',
    data: []
  },
  grid: {
    right: '15%',
  },
  // dataZoom: [
  //   {
  //     type: 'slider',
  //     start: 0,
  //     end: 100
  //   },
  //   {
  //     type: 'inside',
  //     start: 0,
  //     end: 100
  //   }
  // ],
  xAxis: {
    // data: years,
    nameRotate: 45,
    // nameLocation: 'middle',
    name: 'Year',
    axisLabel : {
      fontSize : '12',
    },

  },
  yAxis: {
    min: 0,
    max: 60,
    nameRotate: 45,
    // nameLocation: 'middle',
    name: 'IPRE(%)',
    axisLabel : {
      fontSize : '18',
    },
  },
  series: [
  ],
};

// import raw_data from '../data/sex_male.json';




function updateIpreGraph(keySelect,datapath) {
  fetch(datapath)
  .then(response => response.json())
  .then(json => {
    // copy option_template to option
    let option = JSON.parse(JSON.stringify(option_ipre_template));
    let errorData = [];
    let lineData = [];
    let dataCount;
    let lineCount;

    let raw_data = json;
    console.log(raw_data)
    years = raw_data.years;
    keys = Object.keys(ipre_sub_map[keySelect]);
    data = raw_data.data;
    option.xAxis.data = years;
    dataCount = keys.length;
    lineCount = years.length;
    for(var i = 0; i < dataCount; i++)
    {
      option.legend.data.push(keys[i]);
      option.legend.data.push("95%CI"+keys[i]);
      lineData.push([]);
      errorData.push([]);
      keyLen = data[i].length
      for(var j = 0; j < keyLen; j++)
      {
        lineData[i].push([j+lineCount-keyLen,data[i][j][0]]);
        errorData[i].push([j+lineCount-keyLen, data[i][j][1], data[i][j][2], data[i][j][0]]);
      }
    }
    console.log(lineData);
    console.log(errorData);
    for (var i = 0; i < dataCount; i++)
    {
      option.series.push({
          type: 'line',
          name: keys[i],
          smooth: true,
          data: lineData[i],
          itemStyle: {
            color: colors[i]
          }
        });
      option.series.push({
          type: 'custom',
          name: '95%CI'+keys[i],
          itemStyle: {
            borderWidth: 1.5,
            color: colors[i],
          },
          renderItem: function (params, api) {
            var xValue = api.value(0);
            var highPoint = api.coord([xValue, api.value(1)]);
            var lowPoint = api.coord([xValue, api.value(2)]);
            var halfWidth = api.size([1, 0])[0] * 0.1;
            var style = api.style({
              stroke: api.visual('color'),
              fill: undefined
            });
            return {
              type: 'group',
              children: [
                {
                  type: 'line',
                  transition: ['shape'],
                  shape: {
                    x1: highPoint[0] - halfWidth,
                    y1: highPoint[1],
                    x2: highPoint[0] + halfWidth,
                    y2: highPoint[1]
                  },
                  style: style
                },
                {
                  type: 'line',
                  transition: ['shape'],
                  shape: {
                    x1: highPoint[0],
                    y1: highPoint[1],
                    x2: lowPoint[0],
                    y2: lowPoint[1]
                  },
                  style: style
                },
                {
                  type: 'line',
                  transition: ['shape'],
                  shape: {
                    x1: lowPoint[0] - halfWidth,
                    y1: lowPoint[1],
                    x2: lowPoint[0] + halfWidth,
                    y2: lowPoint[1]
                  },
                  style: style
                }
              ]
            };
          },
          encode: {
            x: 0,
            y: [1, 2],
            tooltip: [3,1,2],
          },
          dimensions: ["year", "low","high","avg"],
          data: errorData[i],
          z: 100
        })
    }
    console.log("ok")
    option && myChart_ipre.setOption(option,true);
  });
}

updateIpreGraph("overall","https://ggpzc.github.io/prearth.github.io/data_preprocessed/ipre/overall.json")
// updateIpreGraph("../data_preprocessed/ipre/overall.json")

// sleep for 5 seconds

// setTimeout(() => {
//   updateGraph("../data/age.json")
// }, "3000");

// setTimeout(() => {
//   updateGraph("../data/sex.json")
// }, "3000");



function ipreSelectChange() {
  let objS = document.getElementById("ipreselect");
  let value = objS.options[objS.selectedIndex].value;
  console.log(value)
  datapath = "https://ggpzc.github.io/prearth.github.io/data_preprocessed/ipre/" + value + ".json";
  // datapath = "..data_preprocessed/ipre/" + value + ".json";
  updateIpreGraph(value,datapath);
}
  
window.onresize = function () {
  setTimeout(function () {
    myChart_ipre.resize();
    myChart_arty.resize();
  }, 10);
};

// for (var i = 0; i < dataCount; i++) {
//   categoryData.push('category' + i);
// }
// for (var j = 0; j < lineCount; j++) {
//     errorData.push([]);
//     barData.push([]);
//     for (var i = 0; i < dataCount; i++) {
//       var val = Math.random() * 1000;
      
//       errorData[j].push([
//         i,
//         echarts.number.round(Math.max(0, val - Math.random() * 100)),
//         echarts.number.round(val + Math.random() * 80)
//       ]);
//       barData[j].push(echarts.number.round(val, 2));
//   }
// }








