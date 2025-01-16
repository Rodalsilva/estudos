defmodule Quociente.Soma do
  def quociente(x, p), do: razao(x+p, x*p)
  defp razao(a, b), do: (-1)*(a/b**2)
end
