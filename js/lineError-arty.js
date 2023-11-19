
var chartDom_arty = document.getElementById('lineError-arty');
var myChart_arty = echarts.init(chartDom_arty);
var option_arty_template;


var arty_sub_map;
var colors = ["#D89C7A", "#849B91", "#8A95A9", "#686789", "#B77F70","#88878D","#8A95A9"]
// read data from local position'../data/sex_female.json'



option_arty_template = {
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
    max: 30,
    nameRotate: 20,
    // nameLocation: 'middle',
    name: 'Prevalence(%)',
    axisLabel : {
      fontSize : '18',
    },
  },
  series: [
  ],
};

// import raw_data from '../data/sex_male.json';




function updateArtyGraph(subkey, filename) {
  fetch("https://ggpzc.github.io/prearth.github.io/data_preprocessed/iartypre/" + filename + ".json")
  .then(response => response.json())
  .then(json => {
    // copy option_template to option
    let option = JSON.parse(JSON.stringify(option_arty_template));
    let errorData_RA = [];
    let lineData_RA = [];
    let errorData_OA = [];
    let lineData_OA = [];
    let dataCount;
    let lineCount;

    let raw_data = json;
    console.log(raw_data)
    years = raw_data.years;
    keys = [subkey];
    data = raw_data.data;
    option.xAxis.data = years;
    dataCount = keys.length;
    lineCount = years.length;
    for(var i = 0; i < dataCount; i++)
    {
      option.legend.data.push(keys[i]+'-RA');
      option.legend.data.push("95%CI-"+keys[i]+'-RA');
      option.legend.data.push(keys[i]+'-OA');
      option.legend.data.push("95%CI-"+keys[i]+'-OA');
      lineData_RA.push([]);
      errorData_RA.push([]);
      lineData_OA.push([]);
      errorData_OA.push([]);
      keyLen = data[i].length
      for(var j = 0; j < keyLen; j++)
      {
        lineData_RA[i].push([j+lineCount-keyLen,data[i][j][0]]);
        errorData_RA[i].push([j+lineCount-keyLen, data[i][j][1], data[i][j][2], data[i][j][0]]);
        lineData_OA[i].push([j+lineCount-keyLen,data[i][j][3]]);
        errorData_OA[i].push([j+lineCount-keyLen, data[i][j][4], data[i][j][5], data[i][j][3]]);
      }
    }
    console.log(lineData_RA);
    console.log(errorData_RA);
    console.log(lineData_OA);
    console.log(errorData_OA);
    for (var i = 0; i < dataCount; i++)
    {
      option.series.push({
          type: 'line',
          name: keys[i]+'-RA',
          smooth: true,
          data: lineData_RA[i],
          itemStyle: {
            color: colors[i]
          }
        });
      option.series.push({
          type: 'line',
          name: keys[i]+'-OA',
          smooth: true,
          data: lineData_OA[i],
          itemStyle: {
            color: colors[i+1]
          }
        });
      option.series.push({
          type: 'custom',
          name: '95%CI-'+keys[i]+'-RA',
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
          data: errorData_RA[i],
          z: 100
        })
      option.series.push({
          type: 'custom',
          name: '95%CI-'+keys[i]+'-OA',
          itemStyle: {
            borderWidth: 1.5,
            color: colors[i+1],
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
          data: errorData_OA[i],
          z: 100
        })
    }
    console.log("ok")
    option && myChart_arty.setOption(option,true);
  });
}





// setTimeout(() => {
//   updateArtyGraph("overall","overall.overall")
// }, "500");


// updateArtyGraph("../data_preprocessed/iartypre/overall.overall.json")
// sleep for 5 seconds

// setTimeout(() => {
//   updateGraph("../data/age.json")
// }, "3000");

// setTimeout(() => {
//   updateGraph("../data/sex.json")
// }, "3000");



// fetch("../data_preprocessed/key_mapping.json")
// fetch("https://ggpzc.github.io/prearth.github.io/data_preprocessed/key_mapping_zh.json")
//   .then(response => response.json())
//   .then(json => {
//     // copy option_template to option
//     arty_sub_map = json;
//     console.log(arty_sub_map);
//   });





function changeSubSelect(key) {
  let objSub = document.getElementById("ipreselect-arty-sub");
  let oOp = objSub.children;
  // remove all option
  objSub.innerHTML = "";
  // for(let i = 0; i < oOp.length; i++) {
  //   objSub.removeChild(oOp[i]);
  // }

  let subkeys = Object.keys(arty_sub_map[key]);
  console.log(subkeys);
  for (let i = 0; i < subkeys.length; i++) {
    objSub.innerHTML += "<option value=\"" + subkeys[i] + "\">" + subkeys[i] + "</option>";
  }

}

function artySelectChange() {
  let objSub = document.getElementById("ipreselect-arty-sub");
  let objS = document.getElementById("ipreselect-arty");
  
  let key = objS.options[objS.selectedIndex].value;
  changeSubSelect(key);

  let subkey = objSub.options[objSub.selectedIndex].value;

  value = arty_sub_map[key][subkey]
  filename = value
  // datapath = "https://ggpzc.github.io/prearth.github.io/data_preprocessed/iartypre/" + value + ".json";
  updateArtyGraph(subkey, filename);
}

function artySubSelectChange() {
  let objSub = document.getElementById("ipreselect-arty-sub");
  let objS = document.getElementById("ipreselect-arty");

  let key = objS.options[objS.selectedIndex].value;
  let subkey = objSub.options[objSub.selectedIndex].value;

  value = arty_sub_map[key][subkey]
  filename = value
  // datapath = "https://ggpzc.github.io/prearth.github.io/data_preprocessed/iartypre/" + value + ".json";
  // datapath = "../data_preprocessed/iartypre/" + value + ".json";
  updateArtyGraph(subkey, filename);
}
  

  

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








