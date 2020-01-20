import pygame
import json
from vector3 import *


class Mesh:
    def __init__(self, name = "UnknownMesh"):
        self.name = name
        self.polygons = []

    def offset(self, v):
        new_polys = []
        for poly in self.polygons:
            new_poly = []
            for p in poly:
                new_poly.append(p + v)
            new_polys.append(new_poly)

        self.polygons = new_polys

    def render(self, screen, matrix, material):
        c = material.color.tuple3()        

        for poly in self.polygons:
            tpoly = []
            for v in poly:
                vout = v.to_np4()
                vout = vout @ matrix
                
                tpoly.append( ( screen.get_width() * 0.5 + vout[0] / vout[3], screen.get_height() * 0.5 - vout[1] / vout[3]) )

            #pygame.draw.polygon(screen, c, tpoly, material.line_width)
            pygame.draw.polygon(screen, c, tpoly)


    @staticmethod
    def create_cube(size, mesh = None):
        if (mesh == None):
            mesh = Mesh("UnknownCube")

        Mesh.create_quad(vector3( size[0] * 0.5, 0, 0), vector3(0, -size[1] * 0.5, 0), vector3(0, 0, size[2] * 0.5), mesh)
        Mesh.create_quad(vector3(-size[0] * 0.5, 0, 0), vector3(0,  size[1] * 0.5, 0), vector3(0, 0, size[2] * 0.5), mesh)

        Mesh.create_quad(vector3(0,  size[1] * 0.5, 0), vector3(size[0] * 0.5, 0), vector3(0, 0, size[2] * 0.5), mesh)
        Mesh.create_quad(vector3(0, -size[1] * 0.5, 0), vector3(-size[0] * 0.5, 0), vector3(0, 0, size[2] * 0.5), mesh)

        Mesh.create_quad(vector3(0, 0,  size[2] * 0.5), vector3(-size[0] * 0.5, 0), vector3(0, size[1] * 0.5, 0), mesh)
        Mesh.create_quad(vector3(0, 0, -size[2] * 0.5), vector3( size[0] * 0.5, 0), vector3(0, size[1] * 0.5, 0), mesh)

        return mesh

    @staticmethod
    def create_quad(origin, axis0, axis1, mesh):
        if (mesh == None):
            mesh = Mesh("UnknownQuad")

        poly = []
        poly.append(origin + axis0 + axis1)
        poly.append(origin + axis0 - axis1)
        poly.append(origin - axis0 - axis1)
        poly.append(origin - axis0 + axis1)

        mesh.polygons.append(poly)

        return mesh

    @staticmethod
    def create_pyramid(vertex, mesh = None):
        if (mesh == None):
            mesh = Mesh("UnknownPyramid")

        Mesh.create_triangle(vertex[0], vertex[1], vertex[2], mesh)
        Mesh.create_triangle(vertex[0], vertex[1], vertex[3], mesh)
        Mesh.create_triangle(vertex[0], vertex[2], vertex[3], mesh)
        Mesh.create_triangle(vertex[1], vertex[2], vertex[3], mesh)

        return mesh

    @staticmethod
    def create_from_json(filename, mesh = None):
        if (mesh == None):
            mesh = Mesh("UnknownMesh")

        verts = []
        faces = []

        with open(filename) as json_file:
            data = json.load(json_file)
            for v in data['vertices']:
                verts.append(vector3(v[0], v[1], v[2]))
            for f in data['faces']:
                faces.append(f)
        
        for f in faces:
            Mesh.create_triangle(verts[f[0]-1], verts[f[1]-1], verts[f[2]-1])

        return mesh


    @staticmethod
    def create_triangle(v1, v2, v3, mesh = None):
        if (mesh == None):
            mesh = Mesh("UnknownTri")
        
        poly = []
        poly.append(v1)
        poly.append(v2)
        poly.append(v3)

        print("face:")
        print(v1)
        print(v2)
        print(v3)
        
        mesh.polygons.append(poly)

        return mesh
