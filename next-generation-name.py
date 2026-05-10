#!/usr/bin/env -S python3 -B
# -*- mode: python; coding: utf-8; python-indent-offset: 2; indent-tabs-mode: nil -*-

import os ,sys

def CLI(argv=None) -> int:
  # Ordered list of renames: files first, then directories to preserve paths
  substitutions = [
    # Administrator
    ("administrator/document/Release_howto.html" ,"administrator/document/how-to_release.html")
    
    # Developer
    ,("developer/document/File_directory_naming.html" ,"developer/document/naming_file-and-directory.html")
    ,("developer/document/RT_code_format.html" ,"developer/document/format_RT-code.html")
    ,("developer/document/Single-file_C_modules_and_namespaces.html" ,"developer/document/single-file_C-module-and-namespace.html")
    ,("developer/tool/do_all" ,"developer/tool/do-all")
    
    # Top-level documents
    ,("document/Introduction_to_Harmony.html" ,"document/introduction_Harmony.html")
    ,("document/Product-development_roles-and-workflow.html" ,"document/role-and-workflow_product-development.html")
    ,("document/Product-maintenance_roles-and-workflow.html" ,"document/role-and-workflow_product-maintenance.html")
    
    # Shared tools and documents
    ,("shared/document/install_Python.org" ,"shared/document/installation_Python.org")
    ,("shared/document/install_generic.org" ,"shared/document/installation_generic.org")
    ,("shared/style_directory_dict.js" ,"shared/dictionary_style-directory.js")
    ,("shared/tool/RTfmt" ,"shared/tool/RT-formatter")
    ,("shared/tool/RTfmt.el" ,"shared/tool/RT-formatter.el")
    ,("shared/tool/makefile/target_kmod.mk" ,"shared/tool/makefile/target_kernel-module.mk")
    
    # Tester files (referenced by the old directory name before it is renamed)
    ,("tester/RT_format/RT_Format.el" ,"tester/RT_format/RT-formatter.el")
    ,("tester/RT_format/RT_format.el" ,"tester/RT_format/RT-formatter_alt.el")
    ,("tester/RT_format/RTfmt" ,"tester/RT_format/RT-formatter")
    ,("tester/RT_format/RTfmt.el" ,"tester/RT_format/RT-formatter_script.el")
    ,("tester/RT_format/RTfmt_with_compare" ,"tester/RT_format/RT-formatter_with-compare")
    ,("tester/RT_format/RTfmt_with_compare.el" ,"tester/RT_format/RT-formatter_with-compare.el")
    ,("tester/RT_format/test_0_data.c" ,"tester/RT_format/data_test-0.c")
    ,("tester/RT_format/test_1_data.py" ,"tester/RT_format/data_test-1.py")
    
    # Directories
    ,("shared/third_party" ,"shared/linked-project")
    ,("tester/RT_format" ,"tester/RT-formatter")
  ]

  for src ,dst in substitutions:
    if not os.path.exists(src):
      print(f"Skipping (not found): {src}")
      continue
    
    if os.path.exists(dst):
      print(f"Warning: Destination {dst} already exists. Skipping rename for {src}.")
      continue
      
    try:
      os.rename(src ,dst)
      print(f"Renamed: {src} -> {dst}")
    except Exception as e:
      print(f"Error renaming {src} to {dst}: {e}")

  return 0

if __name__ == "__main__":
  sys.exit(CLI())

