import rutpy
def validate(rut: str) -> bool:
    return rutpy.validate(rut)
if __name__ == "__main__":
    rut= "21.063.252-2"
    print(validate(rut))

