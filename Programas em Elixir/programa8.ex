defmodule ExpressaoQuadratica do
  defmodule Multiplique do
    def produto(p, x) do
      p*x
    end
  end
end
defmodule Quadrado do
  def quadrado(x) do
    x**2
  end
end
defmodule ExpressaoQuadratica.Multiplique.Quadrado do
  def combinacao(x, p) do
    x**2 + p*x + p**2
  end
end
