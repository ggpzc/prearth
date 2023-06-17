// fetch("../data_preprocessed/key_mapping_iarty.json")
fetch("https://ggpzc.github.io/prearth.github.io/data_preprocessed/key_mapping_iarty.json")
  .then(response => response.json())
  .then(json => {
    // copy option_template to option
    arty_sub_map = json;

    console.log(arty_sub_map);
  });

  // fetch("../data_preprocessed/key_mapping_ipre.json")
  fetch("https://ggpzc.github.io/prearth.github.io/data_preprocessed/key_mapping_ipre.json")
  .then(response => response.json())
  .then(json => {
    // copy option_template to option
    ipre_sub_map = json;

    console.log(arty_sub_map);
  });

init_overall = "overall"