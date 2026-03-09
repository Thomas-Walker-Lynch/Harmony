# tool/shared/Harmony.mk
# makefile environment variable defaults.
# cc is the name of the C compiler, a file called <name>.c is C source code.
# RT uses header integrated C source files, i.e. the source and the header are the same file

SHELL=/bin/bash

ECHO := printf "%b\n"

C_SOURCE_DIR     ?= authored
C                ?= gcc
CFLAGS           ?= -std=gnu11 -Wall -Wextra -Wpedantic -finput-charset=UTF-8
CFLAGS           += -MMD -MP
CFLAGS           += -include "$(REPO_HOME)/shared/tool/makefile/RT_global.h"
CFLAGS           += -I $(C_SOURCE_DIR)


# Project administrators can override this in their local makefile
LIBRARY_NAME     ?= $(PROJECT)
LIBRARY_NAME     := $(subst -,_,$(LIBRARY_NAME))

BUILD_DIR        ?= scratchpad/build
OBJECT_DIR       ?= $(BUILD_DIR)/object
LIBRARY_DIR      ?= scratchpad/made
MACHINE_DIR      ?= scratchpad/made

LIBRARY_FILE     ?= $(LIBRARY_DIR)/lib$(LIBRARY_NAME).a

LN_FLAGS         ?= -L$(LIBRARY_DIR) -L/lib64 -L/lib -l$(LIBRARY_NAME)

KMOD_SOURCE_DIR  ?= authored
KMOD_CCFLAGS     ?= -I $(KMOD_SOURCE_DIR)
# Pass the global header to Kbuild exactly as done for user-space
KMOD_CCFLAGS     += -include $(REPO_HOME)/shared/tool/makefile/RT_global.h
KMOD_OUTPUT_DIR  ?= scratchpad/kmod
