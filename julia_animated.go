package main

import (
	"fmt"
	"image"
	"image/color"
	"image/gif"
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
			real := xMin + float64(x)*(xMax-xMin)/float64(width)
			imag := yMin + float64(y)*(yMax-yMin)/float64(height)
			z := complex(real, imag)

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

// CreatePalettedImage converts iteration data to paletted image for GIF
func CreatePalettedImage(iterations [][]int, maxIter int) *image.Paletted {
	height := len(iterations)
	width := len(iterations[0])

	// Create palette (256 colors)
	palette := make(color.Palette, 256)
	for i := 0; i < 256; i++ {
		t := float64(i) / 255.0
		r := uint8(255 * t)
		g := uint8(255 * t * t)
		b := uint8(255 * t * t * t)
		palette[i] = color.RGBA{r, g, b, 255}
	}

	img := image.NewPaletted(image.Rect(0, 0, width, height), palette)

	for y := 0; y < height; y++ {
		for x := 0; x < width; x++ {
			iter := iterations[y][x]
			colorIndex := uint8((iter * 255) / maxIter)
			img.SetColorIndex(x, y, colorIndex)
		}
	}
	return img
}

// CreateAnimatedGIF generates an animated GIF of Julia sets
func CreateAnimatedGIF() {
	width, height := 200, 200 // Smaller for faster generation
	maxIter := 30
	frames := 32

	fmt.Println("Creating animated Julia set GIF...")

	var images []*image.Paletted
	var delays []int

	for frame := 0; frame < frames; frame++ {
		// Move c around a circle
		angle := float64(frame) * 2 * math.Pi / float64(frames)
		radius := 0.7885
		cParam := complex(radius*math.Cos(angle), radius*math.Sin(angle))

		fmt.Printf("Frame %d/%d: c = %.3f%+.3fi\n", frame+1, frames, real(cParam), imag(cParam))

		// Generate Julia set
		iterations := JuliaSet(cParam, width, height, maxIter)
		img := CreatePalettedImage(iterations, maxIter)

		images = append(images, img)
		delays = append(delays, 10) // 100ms delay between frames
	}

	// Save as animated GIF
	file, err := os.Create("julia_animation.gif")
	if err != nil {
		fmt.Printf("Error creating GIF file: %v\n", err)
		return
	}
	defer file.Close()

	err = gif.EncodeAll(file, &gif.GIF{
		Image: images,
		Delay: delays,
	})

	if err != nil {
		fmt.Printf("Error encoding GIF: %v\n", err)
	} else {
		fmt.Println("Animated GIF saved as julia_animation.gif!")
	}
}

func main() {
	CreateAnimatedGIF()
}
