---
title: "PCB design"
draft: false
---

## What is a PCB?

A PCB is a printed circuit board. Essentially, it consists of an insulated board coated with copper pathways that allow current to flow between components. The pathways are created by etching away from a complete coating of copper and by drilling copper-coated holes. The circuit components are then soldered to the board after it is produced. 

## Layers of a PCB

![layers of a PCB](/img/pcb-fabrication-layers.jpg)

## What software?

You should use [Kicad](https://kicad-pcb.org). It's free and open source, which means that once you learn to use it, you can make PCBs as long as you have a computer. You could also try [Eagle](https://www.autodesk.com/products/eagle/overview), which might be a little easier to use, but it requires a subscription if you want to make a commercial board bigger than this chocolate bar that I'm eating. I've designed a few boards in Eagle; neither Kicad nor Eagle is great (though both are improving fairly quickly after a decade or so of stagnation). You could also try a browser-based program like [Upverter](https://upverter.com), but if they shut down their servers, your designs are gone.

If it makes you feel any better, expensive PCB design software, like [Altium Designer](http://altium.com), is also pretty lousy. (I think the general problem the industry is facing is that electrical engineers are a relatively small population, and they're pretty good at figuring out how to use bad software.)

## Learning Kicad

Here's a rough summary of how to use Kicad.

1.  (If you're using a laptop with a trackpad, plug in a real mouse.)
2.  Make a new project.
3.  Add components to the schematic file.
4.  Connect the components together in the schematic.
5.  Associate a footprint with each component.
6.  Generate a netlist from the schematic.
7.  Read the netlist into the PCB file.
8.  If your footprints are all in a stack, right-click > Global Spread and Place > Spread out All Footprints
9.  Make a mechanical outline of the PCB on the Edge.Cuts layer using "Add Graphic Line or Polygon."
10.  Roughly arrange the parts the way you want them.
11.  Place mechanically critical components.
12.  Place the rest of the components and route traces between everything.
13.  Run a design rule check (DRC).
14.  Repeat cycle: schematic/footprints -> gen. netlist -> read netlist -> tweak layout -> run DRC
15.  Submit .kicad_pcb file to OSH Park (or possibly generate Gerber files for another manufacturer).

## Tutorials to get you started

*   [Chris Gammell's video tutorial on Youtube](https://www.youtube.com/watch?v=PlDOnSHkX2c)
*   [Brian Bryce's written tutorial](http://babryce.com/kicad/tutorial.html)
*   [Digikey's Intro to KiCad playlist on Youtube](https://www.youtube.com/watch?v=vaCVh2SAZY4) 

Note that these two tutorials were created before the latest version of KiCad was released, so a few aspects of your KiCad interface might look slightly different. The main steps remain the same, however. For the most up-to-date written tutorial, try KiCad's own "Getting Started in KiCad":
*   [KiCad's Getting Started tutorial](https://docs.kicad-pcb.org/#_getting_started)


## PCB checklist

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
