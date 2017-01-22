# wire-spin
animate a simple wireframe object using vector algebra and matrix transforms

Jan 22, 2017

The purpose of this project is to render and animate, from very basic mathematical
princples (i.e., using no specialized 3d packages), a simple 3d solid, in Python.

The steps needed will be roughly as follows:
    1. Store an object description
        - as a collection of lines in 3d space: vectors and points)
    2. Render this object as lines on a canvas
        - project 3d vectors onto 2d plane, i.e., the screen)
    3. Rotate this object
        - using matrix transformations
        
While I aim to eschew "reinventing the wheel" (for simple canvas drawing, and 
perhaps for things such as the matrix transforms), I simultaneously desire to
balance this with keeping the code "close to the metal"*, for learning purposes.

* Relatively speaking. Python is, after-all, a high-level language.
