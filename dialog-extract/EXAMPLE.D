// creator  : ~/..NearInfinity-20250611/NearInfinity.jar (v2.4-20250611)
// game     : ~/steam/steamapps/common/Project P
// resource : EXAMPLE.DLG
// source   : data/DLGFiles.bif
// dialog   : lang/en_US/dialog.tlk
// dialogF  : (none)

BEGIN ~EXAMPLE~

IF ~  True()
~ THEN BEGIN 0 // from:
  SAY #55077 /* ~This is an example of text that is read.~ */
  IF ~~ THEN REPLY #55079 /* ~This is a response that will proceed to the next dialog.~ */ GOTO 2
  IF ~~ THEN REPLY #57687 /* ~This is a choice that will exit the dialog.~ */ EXIT
END

IF ~~ THEN BEGIN 1 // from: 0.0
  SAY #57767 /* ~This is another example of text that is read, after the first dialog, after the first option is chosen.~ */
  IF ~~ THEN REPLY #57770 /* ~This is a choice that will exit the dialog.~ */ EXIT
END