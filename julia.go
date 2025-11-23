package main

import (
	"fmt"
	"image"
	"image/color"
	"image/png"
	"math"
	"math/cmplx"
	"os"
)

// JuliaSet generates a Julia set for given c parameter
func JuliaSet(cParam complex128, width, height, maxIter int) [][]int {
	xMin, xMax := -2.0, 2.0
	yMin, yMax := -2.0, 2.0
	
	iterations := make([][]int, height)
	for i := range iterations {
		iterations[i] = make([]int, width)
	}
	
	for y := 0; y < height; y++ {
		for x := 0; x < width; x++ {
			// Convert pixel coordinates to complex plane
			real := xMin + float64(x)*(xMax-xMin)/float64(width)
			imag := yMin + float64(y)*(yMax-yMin)/float64(height)
			z := complex(real, imag)
			
			// Julia set iteration
			iter := 0
			for iter < maxIter && cmplx.Abs(z) <= 2 {
				z = z*z + cParam
				iter++
			}
			iterations[y][x] = iter
		}
	}
	return iterations
}

// CreateImage converts iteration data to PNG image
func CreateImage(iterations [][]int, maxIter int) *image.RGBA {
	height := len(iterations)
	width := len(iterations[0])
	
	img := image.NewRGBA(image.Rect(0, 0, width, height))
	
	for y := 0; y < height; y++ {
		for x := 0; x < width; x++ {
			iter := iterations[y][x]
			
			// Hot colormap approximation
			var r, g, b uint8
			if iter == maxIter {
				r, g, b = 255, 255, 255 // White for points in set
			} else {
				// Color based on escape time
				t := float64(iter) / float64(maxIter)
				r = uint8(255 * t)
				g = uint8(255 * t * t)
				b = uint8(255 * t * t * t)
			}
			
			img.Set(x, y, color.RGBA{r, g, b, 255})
		}
	}
	return img
}

// SavePNG saves image to file
func SavePNG(img image.Image, filename string) error {
	file, err := os.Create(filename)
	if err != nil {
		return err
	}
	defer file.Close()
	
	return png.Encode(file, img)
}

// AnimateJulia generates a series of Julia set images
func AnimateJulia() {
	width, height := 400, 400
	maxIter := 50
	frames := 63
	
	fmt.Println("Generating Julia set animation frames...")
	
	for frame := 0; frame < frames; frame++ {
		// Move c around a circle
		angle := float64(frame) * 0.1
		radius := 0.7885
		cParam := complex(radius*math.Cos(angle), radius*math.Sin(angle))
		
		fmt.Printf("Frame %d/%d: c = %.3f%+.3fi\n", frame+1, frames, real(cParam), imag(cParam))
		
		// Generate Julia set
		iterations := JuliaSet(cParam, width, height, maxIter)
		
		// Create and save image
		img := CreateImage(iterations, maxIter)
		filename := fmt.Sprintf("julia_frame_%03d.png", frame)
		
		if err := SavePNG(img, filename); err != nil {
			fmt.Printf("Error saving %s: %v\n", filename, err)
		}
	}
	
	fmt.Println("Animation frames saved!")
	fmt.Println("To create GIF: convert julia_frame_*.png julia_animation.gif")
}

// GenerateFamousJulia creates some well-known Julia sets
func GenerateFamousJulia() {
	width, height := 800, 800
	maxIter := 100
	
	famous := map[string]complex128{
		"dragon":      complex(-0.7269, 0.1889),
		"rabbit":      complex(-0.8, 0.156),
		"cauliflower": complex(0.285, 0.01),
		"lightning":   complex(-0.4, 0.6),
	}
	
	fmt.Println("Generating famous Julia sets...")
	
	for name, cParam := range famous {
		fmt.Printf("Generating %s Julia set: c = %.4f%+.4fi\n", name, real(cParam), imag(cParam))
		
		iterations := JuliaSet(cParam, width, height, maxIter)
		img := CreateImage(iterations, maxIter)
		filename := fmt.Sprintf("julia_%s.png", name)
		
		if err := SavePNG(img, filename); err != nil {
			fmt.Printf("Error saving %s: %v\n", filename, err)
		} else {
			fmt.Printf("Saved %s\n", filename)
		}
	}
}

func main() {
	fmt.Println("Julia Set Generator in Go")
	fmt.Println("========================")
	
	// Generate famous Julia sets
	GenerateFamousJulia()
	
	fmt.Println()
	
	// Generate animation frames
	AnimateJulia()
	
	fmt.Println("\nDone! Check the generated PNG files.")
}