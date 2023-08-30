// fetch("../data_preprocessed/key_mapping_iarty.json")
fetch("https://ggpzc.github.io/prearth.github.io/data_preprocessed/key_mapping_iarty.json")
  .then(response => response.json())
  .then(json => {
    // copy option_template to option
    arty_sub_map = json;
    console.log(arty_sub_map);
    updateArtyGraph("overall","overall.overall")
  });

  // fetch("../data_preprocessed/key_mapping_ipre.json")
  fetch("https://ggpzc.github.io/prearth.github.io/data_preprocessed/key_mapping_ipre.json")
  .then(response => response.json())
  .then(json => {
    // copy option_template to option
    ipre_sub_map = json;
    console.log(arty_sub_map);
    updateIpreGraph(init_overall,"https://ggpzc.github.io/prearth.github.io/data_preprocessed/ipre/overall.json")
  });

init_overall = "overall"