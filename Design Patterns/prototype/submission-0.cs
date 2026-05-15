public interface IShape {
    IShape Clone();
}

public class Rectangle : IShape {
    private int width;
    private int height;

    public Rectangle(int width, int height) {
        this.width = width;
        this.height = height;
    }

    public int GetWidth() {
        return this.width;
    }

    public int GetHeight() {
        return this.height;
    }

    public IShape Clone() {
        return new Rectangle(this.GetWidth(), this.GetHeight());
    }
}

public class Square : IShape {
    private int length;

    public Square(int length) {
        this.length = length;
    }

    public int GetLength() {
        return this.length;
    }

    public IShape Clone() {
        return new Square(this.GetLength());
    }
}

public class Test {
    public List<IShape> CloneShapes(List<IShape> shapes) {
        var res = new List<IShape>();
        foreach(var shape in shapes){
            res.Add(shape.Clone());
        }
        return res;
    }
}
