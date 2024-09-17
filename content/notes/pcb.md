---
title: "PCB design/Kicad"
draft: false
---

## What is a PCB?

A PCB is a printed circuit board. Essentially, it consists of an insulated board coated with copper pathways that allow current to flow between components. The pathways are created by etching away from a complete coating of copper and by drilling copper-coated holes. The circuit components are then soldered to the board after it is produced. 

![PCB from old ME 30 project](/img/pcb-from-me93.jpg)
Here's a purple PCB from OSHPark. Note that the power jack is oriented in such a way that the power cord would intersect with other parts on the board. This is the kind of detail that is really hard to get right on the first try.

## Layers of a PCB

![layers of a PCB](/img/pcb-fabrication-layers.jpg)

## What software?

You should use [Kicad](https://www.kicad.org/). It's free and open source, which means that once you learn to use it, you can make PCBs as long as you have a computer. You could also try [Eagle](https://www.autodesk.com/products/eagle/overview), which might be a little easier to use, but it requires a subscription if you want to make a commercial board bigger than this chocolate bar that I'm eating. I've designed a few boards in Eagle; neither Kicad nor Eagle is great (though both are improving fairly quickly after a decade or so of stagnation). You could also try a browser-based program like [Upverter](https://upverter.com), but if they shut down their servers, your designs are gone.

If it makes you feel any better, expensive PCB design software, like [Altium Designer](http://altium.com), is also pretty lousy. (I think the general problem the industry is facing is that electrical engineers are a relatively small population, and they're pretty good at figuring out how to use bad software.)

## Learning Kicad

Here's a rough summary of how to use Kicad.

### Preparation Steps

1.  Make sure you have a working breadboard prototype of your circuit.
2.  Draw a schematic diagram of your circuit on paper, so you know what you are trying to re-create on Kicad.
3.  Determine any physical constraints for your final printed circuit board: its ideal length and width, any components that need to be in a specific location (e.g., to match up with breadboard holes or allow for plug access). 
4.  (If you're using a laptop with a trackpad, plug in a real mouse.)

### Steps with the Software
5.  Open Kicad
6.  Make a new project.
7.  Enter the Schematic Editor.
8.  Add components to the schematic file.
9.  Wire the components together in the schematic.
10.  Assign a footprint to each component ("Tools" menu).
11.  "Update PCB from Schematic" ("Tools" menu) to generate a netlist from the schematic.
12.  Enter the PCB Editor.
13.  If your footprints are all in a stack, right-click > Global Spread and Place > Spread out All Footprints
14.  Make a mechanical outline of the PCB on the Edge.Cuts layer using "Add Graphic Line or Polygon."
15.  Roughly arrange the parts the way you want them.
16.  Place mechanically critical components.
17.  Place the rest of the components and route traces between everything.
18.  Run a design rule check (DRC). (Kicad calls this an ERC, but nobody else does.)
19.  Repeat cycle: schematic/footprints -> gen. netlist -> read netlist -> tweak layout -> run DRC
20.  Submit .kicad_pcb file to OSH Park (or possibly generate Gerber files for another manufacturer).

### Keyboard Shortcuts
{{< hint danger >}}
**Tip: Use the KiCad ["hot key keyboard shortcuts"](/img/KiCAD-hotkeys.pdf) to more easily move, rotate, and label components in your schematic and layout.**
{{< /hint >}}

### Overview of KiCad Workflow

![KiCad Schematic Editor flowchart](/img/KiCad_Flowchart1.jpg)

![KiCad PCB Editor flowchart](/img/KiCad_Flowchart2.jpg)

## Tutorials to get you started

*   [Chris Gammell's video tutorial on Youtube](https://www.youtube.com/watch?v=PlDOnSHkX2c)
*   [Brian Bryce's written tutorial](http://babryce.com/kicad/tutorial.html)
*   [Digikey's Intro to KiCad playlist on Youtube](https://www.youtube.com/watch?v=vaCVh2SAZY4) 

Note that the first two tutorials above were created before the latest version of KiCad was released, so a few aspects of your KiCad interface might look slightly different. The main steps remain the same, however. For the most up-to-date written tutorial, try KiCad's own "Getting Started in KiCad":
*   [KiCad's Getting Started tutorial](https://docs.kicad.org/7.0/en/getting_started_in_kicad/getting_started_in_kicad.html)


## General PCB checklist (not applicable to every project)

*   <input type="checkbox"> Mounting holes
*   <input type="checkbox"> Power and ground connector on board
*   <input type="checkbox"> Connector pins labeled
*   <input type="checkbox"> Pin labels not covered by connector bodies
*   <input type="checkbox"> All designators legible, not obscured by vias, oriented the same way, if possible
*   <input type="checkbox"> Power LED, if you can fit one
*   <input type="checkbox"> Testpoints on critical lines, if pins too small to probe
*   <input type="checkbox"> Two grounded holes (can be the same footprints used for connector pins) to solder in a wire loop for scope ground clip
*   <input type="checkbox"> Date, project name, board revision number
*   <input type="checkbox"> Protection circuitry on interfaces (overvoltage zeners, reverse polarity diodes)
*   <input type="checkbox"> You did actually run a design rule check, right?
*   <input type="checkbox"> No design rules "temporarily" loosened?
*   <input type="checkbox"> Drill sizes in allowable range for manufacture
*   <input type="checkbox"> Test upload files with manufacturer, if possible

## PCB gallery

![PCBs for precision voltage shield by Brandon Stafford](/img/pcb-precision-voltage-shield.jpg)
I (Brandon) used to run a company where I manufactured and sold these small Arduino shields. The shield turns your Arduino into an 8-channel voltmeter, and you can stack them to get more channels.

The shrink-wrapped pile is how the PCBs arrived from China, the empty PCB is before I soldered anything on, and the other device has all the components soldered on. Notice that the PCB is a mix of surface-mount (abbreviated SMT or SMD, for surface-mount device) and through-hole components. Today, surface-mount components are preferred for almost everything except connectors, where the strong mechanical connection to the PCB provided by the through-hole is valuable. But, for prototyping, SMT stuff is a nightmare.

![PCB from A123 with conformal coating](/img/pcb-a123-conformal-coating.jpg)
Speaking of nightmares, here's an insane PCB from now-defunct battery manufacturer A123, formerly in Watertown, MA. The PCB is a charge controller from a huge battery pack; its job was to monitor every cell in the pack, and make sure that they were all charged equally and that none of them got too hot. Prototyping this was probably really difficult-- I would bet they made smaller versions first to validate the circuit before they made the whole thing.

Note also that the PCB is covered in a conformal coating (AKA shiny goo). This is to protect the circuit from dust and moisture. Enough dirt and oil piling up on a PCB can make new, slightly conductive paths between pins, which can cause problems for some circuits.

![PCB from Rascal by Brandon Stafford](/img/pcb-rascal.jpg)
This PCB consumed six months of my life. It is the most complex engineering project I have ever completed. The central chip, an Atmel AT91SAM9G20 ARM processor running at 396 MHz, is a ball-grid array package, which means that there is a grid-shaped array of metal balls under the chip instead of pins around the outside. It is risky to solder this kind of chip yourself, because if you get solder blobs underneath shorting out pins, you can't see them without an X-ray machine.

This PCB is also the only PCB I've worked on where the length of the traces mattered. The memory signals on the board are running at 133 MHz, so if one memory trace is a lot longer than another, the nanosecond differences in the time it takes for signals to propagate down the length of the trace mean that a clock cycle can end before all the signals arrive. In the case of this board, it meant that everything went fine, until you tried to do a particularly write-heavy operation (specifically, cloning a git repository) at which point, a signal would arrive late, so the CPU would find an invalid instruction in its memory and reset. I had to revise the board to make all the traces much closer to each other in length. I blogged about [the details of this painful experience](https://rascalmicro.com/2012/05/01/delayed-by-memory-timing-errors/).

![PCB from Rascal 2 by Brandon Stafford](/img/pcb-rascal-2.jpg)
This PCB is cool just because I used black soldermask and yellow silkscreen to make it look cool, but no more expensive than any other board.

![PCB shaped like a rocket by Brandon Stafford](/img/pcb-rocket-dmx.jpg)
Here are some fanciful PCBs I made a few years ago. The rocket engine is actually a DMX connector; the thing is used to control stage lights. This is just to give you the idea that PCBs don’t just have to be boring rectangular things. I made this PCB using weird open-source software called PCBmodE: https://github.com/boldport/pcbmode. If you want to make a simple, but oddly shaped, PCB, maybe that would work for you.

![More PCBs shaped like rockets by Brandon Stafford](/img/array-of-rocket-pcbs.jpg)

## PCB design tips from former ME 30 students

### Lessons learned from Gus, Emily, and Alex:

* figuring out how to ground things
* the circuit doesn’t actually have to complete a circle
* realizing that the rats nest is a guide for how to lay your traces
* you can use any footprint that fits your component
* how to lay components in series vs. parallel in the schematic

### From Ronan, Teddy, Majeed, Matias:

* Finding footprints was very time consuming
* KiCAD schematic is mainly symbolic not functional (not for running a simulation)
* Difficult UI on KiCAD
* Learning keyboard shortcuts for KiCAD was useful
* Sometimes you need to go online to get footprints for parts not on KiCAD
* You can trace on both sides of the board - there are two layers
* Datasheets were a very useful resource
* YouTube is an amazing resource
* A solid understanding of the circuit schematic helped with the production of the PCB later on

### From Jake, Charvady, Alanna, and Trevor:

* Completely new software to all of us - all developed a basic understanding after P1
* All thought kicad was easy-to-use after the learning curve. 
* Demo video was really helpful
* Updating libraries was hard to figure out and not explicitly clear at all
* Assigning the footprints and making sure you had the correct one. Flipping back between all datasheets
* Going back to circuit diagram and being able to update PCB layout directly. 
* All the different layers of the PCB board and deciding which layer is used for what - 2 copper wire layers, top & bottom silk screen.
* Making sure things were facing in the right direction - barrel jack.
* Always had to be thinking of overall PCB layout - wiring and placing components. 
* What to label. When in doubt, label everything. 
* Where to place connector pins and how to connect in circuit diagram.

### From other groups:

* Troubleshooting issues: close the whole application and restart (“brain refresh”)
* Finding components: google main header, some are named weirdly
* Using a mouse instead of a trackpad
* Making schematic traceable and obvious, including labels, etc.
* Use ground symbols instead of connecting things to ground itself
* Don’t want overlap traces in contact
* Learn shortcut keys (example shift + M to move a component)
* Start by building it in a large area, and once you get the hang of it start minimize the area
* If components start to heat up, something is wired wrong
* Good practice: check all the wiring before you plug your circuit into a power source
*	How to look up all the components of the circuit in the library
*	Using the 3D viewer
*	Placing wires on top and bottom layer
*	Condensing components
*	Kicad makes suggestions based on schematic 
*	Labeling pcb board on silk screen
*	Using hot keys (M, R, E, etc.)
*	Placing what you want to plug other things into in an easily accessible spot
