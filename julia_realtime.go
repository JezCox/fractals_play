package main

import (
	"image/color"
	"math"
	"math/cmplx"

	"github.com/hajimehoshi/ebiten/v2"
)

const (
	screenWidth  = 400
	screenHeight = 400
	maxIter      = 50
)

type Game struct {
	frame int
}

// JuliaSet generates Julia set and returns color data
func (g *Game) JuliaSet(cParam complex128) []color.RGBA {
	xMin, xMax := -2.0, 2.0
	yMin, yMax := -2.0, 2.0
	
	colors := make([]color.RGBA, screenWidth*screenHeight)
	
	for y := 0; y < screenHeight; y++ {
		for x := 0; x < screenWidth; x++ {
			// Convert pixel to complex plane
			real := xMin + float64(x)*(xMax-xMin)/float64(screenWidth)
			imag := yMin + float64(y)*(yMax-yMin)/float64(screenHeight)
			z := complex(real, imag)
			
			// Julia iteration
			iter := 0
			for iter < maxIter && cmplx.Abs(z) <= 2 {
				z = z*z + cParam
				iter++
			}
			
			// Color mapping
			var r, g, b uint8
			if iter == maxIter {
				r, g, b = 255, 255, 255
			} else {
				t := float64(iter) / float64(maxIter)
				r = uint8(255 * t)
				g = uint8(255 * t * t)
				b = uint8(255 * t * t * t)
			}
			
			colors[y*screenWidth+x] = color.RGBA{r, g, b, 255}
		}
	}
	return colors
}

func (g *Game) Update() error {
	g.frame++
	return nil
}

func (g *Game) Draw(screen *ebiten.Image) {
	// Animate c parameter around a circle
	angle := float64(g.frame) * 0.05
	radius := 0.7885
	cParam := complex(radius*math.Cos(angle), radius*math.Sin(angle))
	
	// Generate Julia set
	colors := g.JuliaSet(cParam)
	
	// Draw pixels
	for y := 0; y < screenHeight; y++ {
		for x := 0; x < screenWidth; x++ {
			screen.Set(x, y, colors[y*screenWidth+x])
		}
	}
}

func (g *Game) Layout(outsideWidth, outsideHeight int) (int, int) {
	return screenWidth, screenHeight
}

func main() {
	ebiten.SetWindowSize(screenWidth, screenHeight)
	ebiten.SetWindowTitle("Real-time Julia Set Animation")
	
	if err := ebiten.RunGame(&Game{}); err != nil {
		panic(err)
	}
}