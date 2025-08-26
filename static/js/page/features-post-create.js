"use strict";

$("select").selectric();
$.uploadPreview({
  input_field: "#image-upload",  
  preview_box: "#image-preview",
  label_field: "#image-label",    
  label_default: "Choose File",   
  label_selected: "Change File",  
  no_label: false,                
  success_callback: null          
});
$(".inputtags").tagsinput('items');
