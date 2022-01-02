rotate(a = [0,0,z_rotate])
resize(newsize=[x_resize,y_resize,z_resize],auto=true)
linear_extrude(height =model_height)
  offset(r = object_outline_diameter) {
    import(file = model_path, dpi = model_dpi);
  }
