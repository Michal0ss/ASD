# Zadanie 1. (Black Forest) Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las
# składa się z n drzew rosnących na pozycjach 0,..., n-1. Dla każdego i € {0,...,n—1} znany jest zysk c_i, jaki
# można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać maksymalny zysk ze ścinanych
# drzew, ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować algorytm, dzięki któremu
# John znajdzie optymalny plan wycinki.

# f(i) = największy zysk ze ściętych drzew do pozycji i (nie koniecznie drzewo z pozycji i zostało ścięte)
# f(i) = max { f(i - 1), f(i - 2) + C[i] } - albo nie ścinamy drzewa, albo ścinamy

# przypadki graniczne:
# f(0) = C[0]
# f(1) = max {f(0), C[1]}

# wynik f(n - 1)

# Powinna wystarczyć tylko jedna tablica, gdzie nadpisujemy z każdym następnym.

# O(n)

import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Use a valid Windows path (change as needed)
pdf_path = r"C:\Users\Michal0ss\Desktop\wzory_do_zestawu_8.pdf"

c = canvas.Canvas(pdf_path, pagesize=A4)
width, height = A4

c.setFont("Helvetica-Bold", 14)
c.drawCentredString(width / 2, height - 40, "Zestaw wzorow do rozwiazania Zestawu 8 (fizyka)")
c.setFont("Helvetica", 11)

formulas = [
    "1. Wahadlo matematyczne:",
    "   T = 2π * sqrt(l / g)",
    "   f = 1 / T",
    "   v_srednia = droga / czas = (4A) / T",
    "",
    "2. Ruch harmoniczny ciala:",
    "   x(t) = A * cos(ωt) lub A * sin(ωt)",
    "   v(t) = -Aω * sin(ωt), vmax = Aω",
    "   a(t) = -Aω^2 * cos(ωt), amax = Aω^2",
    "   Ep = (1/2) * k * x^2, Ek = (1/2) * m * v^2",
    "   E = (1/2) * k * A^2",
    "   ω = 2π / T",
    "   k = mω^2",
    "",
    "3. Sprezyny:",
    "   Polaczenie szeregowe: 1/keff = 1/k1 + 1/k2",
    "   Polaczenie rownolegle: keff = k1 + k2",
    "   T = 2π * sqrt(m / keff)",
    "",
    "4. Wzory do sprezyny z danymi: vm, am, x1:",
    "   vmax = Aω, amax = Aω^2",
    "   T = 2π * (vm / am), A = vm^2 / am",
    "   k = m * (am / vm)^2",
    "",
    "5. Wahadlo w windzie:",
    "   T = 2π * sqrt(l / g_eff)",
    "   g_eff = g ± a, zalezy od kierunku przyspieszenia",
    "",
    "6. Energia potencjalna - amplituda:",
    "   Ep = mgh, Ep = (1/2) * k * A^2",
    "   A = sqrt(2mgh / k)",
    "",
    "7. Wahadlo fizyczne (pret):",
    "   I = I_srodek + md^2",
    "   d = odleglosc srodka masy od osi",
    "   T = 2π * sqrt(I / (mgr))",
    "   Przykladowo: T = 2π * sqrt(7L / 12g) dla L/4 od konca",
    "",
    "8. Fala mechaniczna:",
    "   y(x,t) = A * sin(ωt - kx)",
    "   f = ω / 2π, T = 1 / f",
    "   v = λ * f, λ = v / f",
    "   k = 2π / λ"
]

y = height - 70
for line in formulas:
    c.drawString(50, y, line)
    y -= 14
    if y < 50:
        c.showPage()
        c.setFont("Helvetica", 11)
        y = height - 50

c.save()