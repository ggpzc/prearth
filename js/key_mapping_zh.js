// fetch("../data_preprocessed/key_mapping_iarty_zh.json")
fetch("https://ggpzc.github.io/prearth.github.io/data_preprocessed/key_mapping_iarty_zh.json")
  .then(response => response.json())
  .then(json => {
    // copy option_template to option
    arty_sub_map = json;

    console.log(arty_sub_map);
  });


  // fetch("../data_preprocessed/key_mapping_ipre_zh.json")
fetch("https://ggpzc.github.io/prearth.github.io/data_preprocessed/key_mapping_ipre_zh.json")
  .then(response => response.json())
  .then(json => {
    // copy option_template to option
    ipre_sub_map = json;

    console.log(arty_sub_map);
  });

init_overall = "总体患病率"