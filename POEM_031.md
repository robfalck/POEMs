POEM ID:  31  
Title:   Global OpenMDAO Settings  
authors: Rob Falck  
Competing POEMs: N/A  
Related POEMs: N/A  
Associated implementation PR: N/A

Status:

- [x] Active
- [ ] Requesting decision
- [ ] Accepted
- [ ] Rejected
- [ ] Integrated


Motivation
----------

Debugging OpenMDAO models frequently involves increasing verbosity of solvers.
For this reason, the method set_solve_print exists to recurse through the model tree and set the noisiness of solvers to the desired level.

This behavior would also be convenient with AnalysisError.
A model could have many components which raise AnalysisError in certain situations, such as meta-models with extrapolation disabled.
When optimizing using SNOPT, a triggered AnalysisError results in a backtracking of the optimziation line search and results in a `D` being desplayed in the iteration status.
Tracking exactly which component triggered that AnalysisError is difficult.
This POEM first proposes adding a `verbose` setting to AnalysisError that will print the file and line number where the AnalysisError was raised.

Description
-----------

1. Verose AnalysisError

Add argument `verbose` to AnalysisError.  If True, AnalysisError's `__init__` should do something like the following:

import inspect
try:
    caller = inspect.getframeinfo(inspect.stack()[1][0])
    print(f'AnalysisError: {caller.filename} - {caller.lineno}')
except IndexError:
    pass

Here the IndexError exception is only a guard against AnalysisError being instantiated directly in a python interpreter without a caller.

2. The Global OptionsDictionary

Rather than down the path of adding a new `set_analysiserror_verbosity` method to problem (and adding a new method every time such functionality is added) seems like it would unnecessarily complicate the API compared to a global options dictionary for certain settings.

```
import openmdao.api as om

om.options['solver_print'] = 2
om.options['verbose_analysis_error'] = True
```

In order to be useful for debugging, these settings have to override any set during the model creation.

A default value of `unspecified` will prevent the behavior defined during model creation from being overridden.

Because these values override system options, they will be recorded.

3. The OpenMDAO settings file

An OpenMDAO settings/preferences file will allow the user to set the default values for certain options.
This file will use Python's configparser module to avoid any external dependencies.
OpenMDAO will first check for a global file (`.openmdao.cfg`) in the user's home directory or default preferences location.
OpenMDAO will next check the current working directory for a file named `.openmdao.cfg` and override the default settings with any found there.

OpenMDAO will allow the user to export a settings file at the command line using:

```
$ openmdao export_settings > my_settings.cfg
```

This will allow users to exchange settings files when sharing models.

Notional Settings File Format
-----------------------------
```
[defaults]
solver_print = -1
verbose_analysiserror = False

[N2]
initial_depth = 5

```
