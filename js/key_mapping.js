fetch("https://ggpzc.github.io/prearth.github.io/data_preprocessed/key_mapping.json")
  .then(response => response.json())
  .then(json => {
    // copy option_template to option
    arty_sub_map = json;
    ipre_sub_map = json;
    console.log(arty_sub_map);
  });