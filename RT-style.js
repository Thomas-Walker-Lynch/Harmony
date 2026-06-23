// RT-style.js
window.RT = window.RT || {};

// Configuration
window.RT.project_name = "RT-style"; 
window.RT.server_url = "http://localhost:8000/shared/linked-project/RT-style/consumer/made";

(function() {
  let style_path = window.RT.server_url;

  if (window.RT.project_name) {
    const path = window.location.pathname;
    const project_root_index = path.indexOf('/' + window.RT.project_name + '/');
    
    if (project_root_index !== -1) {
      const absolute_project_root = path.substring(0, project_root_index + window.RT.project_name.length + 1);
      style_path = absolute_project_root + "/shared/linked-project/RT-style/consumer/made";
    } else {
      console.warn("RT-style: Cannot locate project root '/" + window.RT.project_name + "/'. Falling back to server URL.");
    }
  }
  
  window.RT.dirpr_library = style_path;
  
  // 1. Inject the loader script
  document.write('<script src="' + window.RT.dirpr_library + '/Core/loader.js"><\/script>');
  
  // 2. Inject a secondary script block for the core dependencies.
  // This guarantees the browser waits for loader.js to finish parsing before executing.
  document.write(
    '<script>' +
    'window.RT.load("Core/utility");' +
    'window.RT.load("Core/block_visibility_during_layout");' +
    'window.RT.load("Theme");' +
    'window.RT.load("Element/theme_selector");' +
    '<\/script>'
  );
})();
