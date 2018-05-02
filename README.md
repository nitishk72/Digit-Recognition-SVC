# Digit-Recognition-SVC

## Image as 3D data

    [
      first row
      [
          first column
          [ 0.  0.  0.],  sum/3.0
           . . . . . . . .
          last column
          [ 0.  0.  0.]
      ],
      .  . .  .  .  .
      last row
      [
              first column
              [ 0.  0.  0.]
               .  . . . . .
              last column
               [ 0.  0.  0.]
      ]
     ]

## Converting 3D image into 1D

    for each_row in img:
        for each_pixel in each_row:
            array.append(((sum(each_pixel)) / 3.0))
