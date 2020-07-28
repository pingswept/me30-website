---
title: "Prototyping"
draft: false
---
## Breadboards vs. protoboards vs. PCBs

There are three major ways to build electronics:

1. solderless breadboards, like you have in your project kit
2. protoboards, which are printed circuit boards with a generic grid of useful holes
3. printed circuit boards (PCBs)
4. (plugging together components with connectors, but that's more assembling than building, I would say)

## Breadboards

In the days of yore, when electronic components were big and bulky, we used to prototype by screwing components down to a piece of wood, like a wooden cutting board you would use to cut bread. Hence, "breadboarding."

Now, we use solderless breadboards. The modifier "solderless" is just to distinguish them from protoboards, which are like breadboards, but need solder for assembly.

Here are a few facts about breadboards that are not immediately obvious.

* Each row subsection of 5 pins is connected together, but the two 5 pin subsections are not connected across the central groove.
* The groove is there so that you can plug chips across it and have each pin hit a different group of 5 pins.
* The columns marked with red and blue along the sides are usually used for power and ground. Each column is connected to the rest of itself, but the columns are not connected to each other. It's common to run wires at one end of the board to connect the red column on the left to the one on the right, and same for the blue columns.
* If you stick something really fat into the holes, like a screwdriver or a big diode leg, you might damage the connection inside.

## Protoboards

Once you have a breadboard prototype that works, the next step is to make something less fragile. Sometimes people skip straight to a printed circuit board, but if you only need to make one device, a protoboard can be a faster, robust solution.

## Printed circuit boards 

PCBs are just sheets of fiberglass with copper wires printed on them, along with holes to connect components. They're a big deal, so you can read the details in the [PCB section](/notes/pcb).
