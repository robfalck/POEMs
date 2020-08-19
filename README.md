
# OpenMDAO POEM Process

The POEM process is the official mechanism for proposing, discussing, revising, and ultimately approving or rejecting all changes to the [OpenMDAO](https://openmdao.org) project which effect its user interaction. 
The process involves writing, reading, and discussing documents called POEMs (**p**roposal for **O**penMDAO **e**nhance**m**ent). 

This process governs all API changes, feature additions, and feature removals to the OpenMDAO project. 
It is also recursive because it governs any changes to itself. 

The process serves two primary and equally important purposes: 

1) Announce all changes to the user interface of OpenMDAO to users  
of the framework **before** they are added to the main repository

2) Provide a mechanism for external users to propose  
changes to the user interface for OpenMDAO

## How does it work?

The rules are described in the [POEM_000.md](https://github.com/OpenMDAO/POEMs/blob/master/POEM_000.md) document in this repository. 
The OpenMDAO POEMs repository (i.e. this repo) contains a full record of all POEMs submitted, starting November 1st, 2019. 
Both the core development team and external users participate, and input on any POEM is welcome from any user at any time. 


## How can I keep up to date on POEMs?

All POEM activity is managed within this repository, via PRs and comments to those PRs. 
The best way to track that activity is to star and watch this repository. 
That way, github's built in notification system to get emails when things are changing. 
[Github has lots of great docs on this!](https://help.github.com/en/github/receiving-notifications-about-activity-on-github/watching-and-unwatching-repositories)


## List of POEMs

| POEM ID | Title | Author | Status |
| ------- | ----- | ------ | ------ |
| 000 | POEM Purpose and Guidelines | justinsgray (Justin S. Gray) | active |
| 001 | Units update for better astrodynamics support | [robfalck] | active |
| 002 | New capability for user to send a termination signal to an OpenMDAO process so that SNOPT in pyoptsparse can terminate cleanly. | [Kenneth-T-Moore] | active |
| 003 | Allowing addition if I/O during Configure | anilyil (Anil Yildirim); justinsgray (Justin Gray); robfalck (Rob Falck) | active |
| 004 | Creating Interpolant Class For 1D Splines | [DKilkenny] | active |
| 005 | An OpenMDAO Plugin System | [naylor-b] | active |
| 007 | String Compatibility for ExternalCodeComp and ExternalCodeImplicitComp Command Options | [DKilkenny] (Danny Kilkenny) | active |
| 008 | Nonlinear Solver Refactor | [DKilkenny] (Danny Kilkenny) | active |
| 009 | setup/configure API Changes | @robfalck | active |
| 010 | add argument `recordable` to options.declare | @robfalck | active |
| 011 | Expand problem recording options | @robfalck @hschilling | active |
| 012 | Give the user the option to select the LAPACK driver for use in the SVD used in KrigingSurrogate | [hschilling] ([Herb Schilling]) | active |
| 013 | Unit conversion enhancements | @robfalck | active |
| 014 | Removal of XDSM viewer to be replaced by third-party plugin | @robfalck | active |
| 016 | Linear algebra components can perform multiple calculations. | @robfalck | active |
| 017 | User can specify units when adding design variables, constraints, and objectives. | @Kenneth-T-Moore | active |
| 018 | indices and src_indices can contain slices | @Kenneth-T-Moore | active |
| 019 | Random Vectors in Directional Derivatives | [kejacobson] (Kevin Jacobson) | active |
| 020 | KSComp option to automatically add corresponding constraint | @robfalck | active |
| 021 | _post_configure moved to public API | [robfalck] (Rob Falck) | active |
| 023 | Remove reconfigure code from the current code base | [naylor-b] (Bret Naylor) | active |
| 025 | allow GA to seek pareto frontier | [Kenneth-T-Moore] | active |
| 026 | Remove support for factorial function in ExecComp | [swryan] | active |
| 027 | Approximation flag and state tracking | johnjasa | active |
| 029 | Retrieval of IO Variable Metadata | Bret Naylor | active |

