# Quick Sort:
#
# Recursive
# QuickSort(Data(), left, righ):
#     if Left < Right Then
#         PivotPoistion = Partition(Data, Left, Right)
#         QuickSort(Data, LEft, PivotPoistion -1)
#         QuickSort(Data, PivotPostion + 1, Right)
#     End if
#
#==============================================================
# Alternative:
# WHILE LeftPointer <> RightPointer:
#     While (Data(LeftPointer) < Data(RigthPointer)) AND (LeftPointer <> RightPointer)
#         LeftPointer = LeftPointer + 1
#     End While
#     Temp = Data(LeftPointer)
#     Data(LeftPointer) = Data(RightPointer)
#     Data(RightPointer) = Temp
#     WHILE (Data(LeftPointer) < Data(RightPointer)) And (LeftPointer <> RightPointer)
#         RightPointer = RightPointer - 1
#     End While
#     Emp = Data(LeftPointer)
#     Data(LeftPointer) = Data(RightPointer)
#     Data(RightPointer) = Temp
# End WHILE
#==============================================================
#
# Pivot = Data(LeftPointer)
# While LeftPointer <> RightPointer:
#     If CurrentPointer = "right" Then
#         If Data(RightPointer) < Pivot Then
#             Data(LeftPointer) = Data(RightPointer)
#             LeftPointer = LeftPointer + 1
#             CurrentPointer = "Left"
#         Else:
#             RightPointer = RightPointer - 1
#         End If
#     Elif CurrentPointer = "Left" Then
#         If Data(LeftPointer) > Pivot Then
#             Data(RightPointer) = Data(LeftPointer)
#             RightPointer = RightPointer - 1
#             CurrentPointer = "right"
#         Else
#             LeftPointer = LeftPointer + 1
#         endif
#     Endif
# End While
# Data(LeftPointer) = Pivot
