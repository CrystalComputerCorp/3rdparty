# By default, we expect all submakes to place their products here
RPM_OUTPUT_DIR ?= $(shell pwd)/

# All the variables we will pass to submakes
SUBMAKE_VARS := "RPM_OUTPUT_DIR=$(RPM_OUTPUT_DIR)"

# Find all subdirectories with a Makefile and run the command we are passed there
SUB_DIRS := $(dir $(wildcard */Makefile ) )
TOP_TARGETS := all clean
$(TOP_TARGETS): $(SUB_DIRS)
$(SUB_DIRS):
	@echo [$(patsubst %/,%,$@)]: make $(MAKECMDGOALS)
	@$(MAKE) --no-print-directory $(SUBMAKE_VARS) -C $@ $(MAKECMDGOALS)
.PHONY: $(TOP_TARGETS) $(SUB_DIRS) $(SUB_MAKES)

clean:
	@rm -f *.rpm