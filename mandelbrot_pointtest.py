''' To convince myself how this works, having picked points from the plot'''

def run_test():
    in_set_pt = complex(-0.2, 0.1)  # white
    well_outside_pt = complex(-1.5, -1.0) # black
    fringe_pt = complex(0.4051, 0.3085) # yellow
    on_edge_pt = complex(0.4541, 0.3292) # dark red

    test_for_point(in_set_pt, "In Set Point")
    test_for_point(well_outside_pt, "Well Outside Point")
    test_for_point(fringe_pt, "Fringe Point")
    test_for_point(on_edge_pt, "On Edge Point")

def test_for_point(c, name):
    print(f"\nTesting point: {c} : {name}")

    z = complex(0,0)
    MAX_ITER = 100
    for i in range(MAX_ITER):
        z = z**2 + c
        print("Iteration %d: z = %s, magnitude = %f" % (i, z, abs(z)))
        if abs(z) > 2:
            print(f"Point {c} escapes after {i} iterations (z={z})")
            return



if __name__ == '__main__':
    run_test()