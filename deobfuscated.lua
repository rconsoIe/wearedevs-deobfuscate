return (function(...)
  local K = {
    "w8PAwY==",
    "W+pALBwI",
    "aDTSQomTF76uCoFQyDQ=",
    "RqY2hJDS",
    "WKFJygTMWBSGwMI2",
    "wzSULBc=",
    "EoR9FNdVjjV8xdY7On3yikLapBzouUiP3ngiBv==",
    "rVSZwopxwgTIwkEVW4G=",
    "zJ6tw4n=",
    "WtWYQwRDJhpCuYAKddhE8v==",
    "5V6q54Jswzc=",
    "pPx+1JEy",
    "LKk=",
    "LKc=",
    "zJ6AwzFx5VPsLVQ=",
    "rs3IwuGEr3==",
    "Lo1pF86+CzSmYD105v==",
    "1JEs5QcJio6FiVmlCga=",
    "w8Jx5V1G",
    "4+anii5A5Pko44Em",
    "uB0kK3==",
    "",
    "nQ8TH++y2I/=",
    "OCHJwEn=",
    "Z86qZ8Po",
    "ZOIowY==",
    "5V6M5gSEL+W=",
    "LVpq",
    "5VPsLVQ=",
    "p8xQQIkhWBPVrQIhCv==",
    "1k6lWk5DwJPcpOkU",
    "LP1CiBGMd+xtp+Fb1Ov=",
    "pVPAWVpUckFI5VpD5Vp7cY==",
    "54m/Z41R",
    "r9YlyPsVAuPEoY==",
    "zJ6EL+FIdv==",
    "57AP1D1li+PR",
    "WV1xLV/=",
    "wB1JZ3==",
    "Q8poY86UwY==",
    "CQwMyzGni8ko5B1DiPv=",
    "y4S0Lk11a45aYoJwCV7=",
    "W8poL4poZzFxZ+hI",
    "d76TW86PWPp7ZDTsY4X=",
    "zJ6OZ/==",
    "L4PoCv==",
    "W+PqwV6A",
    "Z8xxW3==",
    "QJ5BapErw4pCwk5o",
    "w+heLBc=",
    "WBFUC4mO",
    "YQAxW7IzYJIxi4xpY3==",
    "r3=="
  }
  local function y(y)
    return K[y + 31466]
  end
  for y, B in ipairs({
    {1, 53},
    {1, 8},
    {9, 53}
  }) do
    while B[1] < B[2] do
      K[B[1]], K[B[2]], B[1], B[2] = K[B[2]], K[B[1]], B[1] + 1, B[2] - 1
    end
  end
  do
    local y = table.concat
    local B = {
      n = 56,
      ["7"] = 36,
      o = 52,
      p = 21,
      h = 49,
      C = 26,
      l = 10,
      ["3"] = 32,
      q = 46,
      ["/"] = 48,
      K = 3,
      ["4"] = 22,
      D = 35,
      e = 47,
      t = 44,
      g = 7,
      S = 9,
      y = 18,
      u = 2,
      ["5"] = 29,
      z = 23,
      A = 45,
      G = 40,
      P = 5,
      N = 62,
      ["6"] = 61,
      a = 12,
      s = 34,
      ["2"] = 15,
      x = 33,
      Q = 20,
      F = 17,
      I = 37,
      U = 50,
      c = 8,
      k = 4,
      w = 25,
      d = 30,
      ["1"] = 13,
      V = 6,
      j = 11,
      H = 31,
      R = 43,
      O = 39,
      ["9"] = 63,
      E = 41,
      r = 14,
      W = 28,
      X = 60,
      Y = 16,
      Z = 24,
      f = 59,
      T = 1,
      J = 53,
      ["0"] = 42,
      L = 27,
      B = 55,
      b = 58,
      ["+"] = 38,
      v = 0,
      ["8"] = 54,
      m = 57,
      i = 19,
      M = 51
    }
    local c = string.len
    local u = table.insert
    local k = type
    local g = K
    local v = string.char
    local I = string.sub
    local Q = math.floor
    for K = 1, #g do
      local l = g[K]
      if k(l) == "string" then
        local k = c(l)
        local Z = {}
        local a = 1
        local d = 0
        local o = 0
        while k >= a do
          local K = I(l, a, a)
          local y = B[K]
          if y then
            d = d + y * 64 ^ (3 - o)
            o = o + 1
            if o == 4 then
              o = 0
              local K = Q(d / 65536)
              local y = Q(d % 65536 / 256)
              local B = d % 256
              u(Z, v(K, y, B))
              d = 0
            end
          elseif K == "=" then
            u(Z, v(Q(d / 65536)))
            if k <= a or I(l, a + 1, a + 1) ~= "=" then
              u(Z, v(Q(d % 65536 / 256)))
            end
            break
          end
          a = a + 1
        end
        g[K] = y(Z)
      end
    end
  end
  return (function(K, c, u, k, g, v, I, i, a, o, j, Q, B, W, z, L, t, f, J, Z, d, l)
    function d(K)
      for y = 1, #K do
        l[K[y]] = l[K[y]] + 1
      end
      if u then
        local B = u(true)
        local c = g(B)
        c[y(-31422)], c[y(-31413)], c[y(-31449)] = K, o, function()
          return 1635854
        end
        return B
      else
        return k({}, {
          [y(-31413)] = o,
          [y(-31422)] = K,
          [y(-31449)] = function()
            return 1635854
          end
        })
      end
    end
    i, Q, B, o, f, J, W, L, j, a, t, l, z, Z = function(K)
      l[K] = l[K] - 1
      if l[K] == 0 then
        l[K], Q[K] = nil, nil
      end
    end, {}, function(B, u, k, g)
      local Y, x, H, A, G, n, F, S, N, b, T, C, o, w, O, R, e, l, d, P, M, I, U, r, q, s, t, a, D, E, m, V, X, h
      while B do
        if B < 9375083 then
          if B < 5767285 then
            if B < 1393592 then
              if B < 1010771 then
                if B < 977583 then
                  if B < 647983 then
                    if B < 125356 then
                      P = nil
                      b = Z()
                      w = nil
                      A = {}
                      h = L(7812337, {
                        b,
                        n,
                        M,
                        t
                      })
                      V = {}
                      Q[b] = V
                      S = y(-31443)
                      V = Z()
                      H = nil
                      Q[V] = h
                      Y = y(-31422)
                      r = Z()
                      h = {}
                      Q[r] = h
                      E = y(-31415)
                      h = K[E]
                      F = Q[r]
                      d = nil
                      I = {}
                      T = nil
                      O = nil
                      s = {
                        [Y] = F,
                        [S] = w
                      }
                      G = nil
                      E = h(A, s)
                      h = f(15195862, {
                        r,
                        b,
                        X,
                        n,
                        M,
                        V
                      })
                      V = i(V)
                      Q[o] = E
                      t = i(t)
                      b = i(b)
                      B = K[y(-31440)]
                      Q[a] = h
                      P = z(7789614, {o, a})
                      M = i(M)
                      X = i(X)
                      r = i(r)
                      o = i(o)
                      n = i(n)
                      t = y(-31420)
                      d = K[t]
                      t = d(P)
                      a = i(a)
                    else
                      U = Q[a]
                      B = U and 16297827 or 9659093
                      R = U
                    end
                  else
                    t = 35184372088832
                    B = {}
                    H = y(-31460)
                    Q[k[2]] = B
                    B = 5165514
                    I = Q[k[3]]
                    o = I
                    O = 255
                    I = a % t
                    Q[k[4]] = I
                    P = a % O
                    O = 2
                    t = P + O
                    Q[k[5]] = t
                    O = K[H]
                    H = y(-31430)
                    P = O[H]
                    O = P(l)
                    H = 1
                    M = 1
                    P = y(-31436)
                    T = M
                    M = 0
                    d[a] = P
                    P = 254
                    n = O
                    X = T < M
                    M = H - T
                  end
                elseif B < 984888 then
                  r = Z()
                  A = 100
                  E = y(-31465)
                  S = 2
                  Q[r] = N
                  I = K[E]
                  E = y(-31464)
                  B = I[E]
                  s = 255
                  E = 1
                  F = 1
                  I = B(E, A)
                  m = 10000
                  E = Z()
                  Q[E] = I
                  B = Q[O]
                  A = 0
                  I = B(A, s)
                  A = Z()
                  Q[A] = I
                  w = y(-31431)
                  s = 1
                  B = Q[O]
                  Y = Q[E]
                  I = B(s, Y)
                  s = Z()
                  Q[s] = I
                  I = Q[O]
                  Y = I(F, S)
                  S = y(-31458)
                  e = 0
                  I = 1
                  B = Y == I
                  Y = Z()
                  I = y(-31442)
                  Q[Y] = B
                  U = K[w]
                  D = Q[O]
                  x = {
                    D(e, m)
                  }
                  w = U(c(x))
                  B = y(-31419)
                  U = y(-31458)
                  R = w .. U
                  B = V[B]
                  F = S .. R
                  S = y(-31420)
                  B = B(V, I, F)
                  F = Z()
                  R = J(3113949, {
                    O,
                    r,
                    M,
                    d,
                    a,
                    b,
                    Y,
                    F,
                    E,
                    s,
                    A,
                    n
                  })
                  Q[F] = B
                  I = K[S]
                  S = {
                    I(R)
                  }
                  B = {
                    c(S)
                  }
                  S = B
                  B = Q[Y]
                  B = B and 7664791 or 171018
                else
                  B = K[y(-31459)]
                  I = {a}
                end
              elseif B < 1248168 then
                if B < 1144730 then
                  if B < 1126653 then
                    B = {}
                    a = 1
                    d = Q[k[9]]
                    o = d
                    d = 1
                    t = d
                    l = B
                    d = 0
                    P = t < d
                    B = 1324773
                    d = a - t
                  else
                    B = U
                    B = 6531550
                    I = R
                  end
                else
                  B = 11634735
                  b = #G
                  h = 0
                  V = b == h
                end
              elseif B < 1325421 then
                d = d + t
                O = not P
                a = o >= d
                a = O and a
                O = o <= d
                O = P and O
                a = O or a
                O = 5641945
                B = a and O
                a = 6123448
                B = B or a
              else
                d = 9311201
                a = y(-31421)
                I = 14997140
                l = a ^ d
                B = I - l
                I = y(-31462)
                l = B
                B = I / l
                I = {B}
                B = K[y(-31414)]
              end
            elseif B < 4799995 then
              if B < 3669658 then
                if B < 2192919 then
                  if B < 1563630 then
                    r = y(-31445)
                    q = y(-31431)
                    B = K[q]
                    h = K[r]
                    q = B(h)
                    B = y(-31444)
                    K[B] = q
                    B = 10446202
                  else
                    B = Q[k[7]]
                    B = B and 13398239 or 1013119
                  end
                else
                  a = Q[k[1]]
                  o = 1
                  t = 2
                  d = a(o, t)
                  a = 1
                  l = d == a
                  I = l
                  B = l and 4246574 or 9175161
                end
              elseif B < 4457579 then
                B = I and 11212123 or 1601068
              else
                a = Q[k[2]]
                d = 33
                l = a * d
                a = 15915310685427
                I = l + a
                l = 35184372088832
                B = I % l
                Q[k[2]] = B
                l = Q[k[3]]
                a = 1
                I = l ~= a
                B = 11883878
              end
            elseif B < 4909260 then
              if B < 4875439 then
                B = true
                B = B and 13238743 or 7893938
              else
                l = y(-31425)
                I = y(-31452)
                B = K[I]
                I = B(l)
                B = K[y(-31441)]
                I = {}
              end
            elseif B < 5248009 then
              G = not X
              M = M + T
              H = n >= M
              H = G and H
              G = n <= M
              G = X and G
              H = G or H
              G = 15085327
              B = H and G
              H = 11638836
              B = B or H
            else
              B = Q[k[1]]
              H = 0
              n = 255
              O = B(H, n)
              a = d
              B = 1324773
              l[a] = O
              a = nil
            end
          elseif B < 7793305 then
            if B < 7244111 then
              if B < 6531078 then
                if B < 6126256 then
                  if B < 6079739 then
                    I = {}
                    B = K[y(-31428)]
                  else
                    B = Q[k[10]]
                    a = Q[k[11]]
                    l[B] = a
                    B = Q[k[12]]
                    a = {
                      B(l)
                    }
                    B = K[y(-31427)]
                    I = {
                      c(a)
                    }
                  end
                else
                  o = i(o)
                  P = nil
                  n = i(n)
                  t = i(t)
                  T = nil
                  O = i(O)
                  O = y(-31465)
                  G = nil
                  b = i(b)
                  d = i(d)
                  P = y(-31465)
                  H = nil
                  n = y(-31460)
                  a = i(a)
                  X = nil
                  a = nil
                  o = Z()
                  M = i(M)
                  T = {}
                  d = nil
                  M = Z()
                  G = {}
                  Q[o] = a
                  V = nil
                  b = 256
                  V = 1
                  a = Z()
                  Q[a] = d
                  t = K[P]
                  H = y(-31429)
                  P = y(-31461)
                  d = t[P]
                  t = Z()
                  Q[t] = d
                  P = K[O]
                  O = y(-31464)
                  d = P[O]
                  O = K[H]
                  H = y(-31456)
                  P = O[H]
                  X = Z()
                  H = K[n]
                  n = y(-31463)
                  O = H[n]
                  H = 0
                  n = Z()
                  Q[n] = H
                  H = 2
                  Q[M] = H
                  Q[X] = T
                  H = {}
                  h = b
                  T = 0
                  B = 14113674
                  b = 1
                  r = b
                  b = 0
                  E = r < b
                  b = V - r
                end
              elseif B < 6654610 then
                Q[a] = I
                B = 7998078
              else
                d = y(-31460)
                B = true
                l = u
                a = Z()
                Q[a] = B
                I = K[d]
                d = y(-31439)
                B = I[d]
                d = Z()
                t = Z()
                Q[d] = B
                H = z(16387775, {t})
                B = f(4875595, {})
                o = Z()
                O = y(-31420)
                Q[o] = B
                B = false
                Q[t] = B
                P = K[O]
                O = P(H)
                B = O and 13859498 or 11419552
                I = O
              end
            elseif B < 7649261 then
              if B < 7454603 then
                x = 2
                D = S[x]
                x = Q[F]
                B = 1144440
                w = D == x
                R = w
              else
                h = 6
                B = Q[O]
                q = 1
                C = B(q, h)
                h = y(-31444)
                B = y(-31444)
                K[B] = C
                q = K[h]
                h = 2
                print(q, h)
                if q > h then
                  -- error("Tamper Detected!")
                end
                B = q > h
                B = B and 1395270 or 15063789
              end
            elseif B < 7767874 then
              R = Q[a]
              B = R and 11507039 or 6531550
              I = R
            else
              t = y(-31423)
              l = y(-31457)
              I = K[l]
              P = 9011713855588
              a = Q[k[1]]
              d = Q[k[2]]
              o = d(t, P)
              l = a[o]
              B = I[l]
              H = 27073614573887
              I = y(-31418)
              t = y(-31448)
              a = Q[k[1]]
              d = Q[k[2]]
              T = 33613001604388
              P = 33626101202218
              o = d(t, P)
              n = 31072255916165
              l = a[o]
              o = Q[k[1]]
              t = Q[k[2]]
              O = y(-31434)
              P = t(O, H)
              d = o[P]
              H = y(-31454)
              X = 19716128973789
              t = Q[k[1]]
              M = 28195734532937
              P = Q[k[2]]
              I = B[I]
              O = P(H, n)
              o = t[O]
              P = Q[k[1]]
              O = Q[k[2]]
              n = y(-31437)
              H = O(n, M)
              t = P[H]
              O = Q[k[1]]
              H = Q[k[2]]
              M = y(-31451)
              n = H(M, T)
              P = O[n]
              H = Q[k[1]]
              T = y(-31435)
              n = Q[k[2]]
              M = n(T, X)
              O = H[M]
              H = 3
              a = {
                [d] = o,
                [t] = P,
                [O] = H
              }
              I = I(B, l, a)
              I = {}
              B = K[y(-31453)]
            end
          elseif B < 8201221 then
            if B < 7957065 then
              if B < 7862326 then
                if B < 7820885 then
                  l = Q[k[1]]
                  I = #l
                  l = 0
                  B = I == l
                  B = B and 4755826 or 14152006
                else
                  B = j(10163996, {o})
                  C = {
                    B()
                  }
                  B = K[y(-31416)]
                  I = {
                    c(C)
                  }
                end
              else
                I = {}
                B = K[y(-31417)]
              end
            elseif B < 7993435 then
              I = n
              B = M
              B = n and 14610855 or 13670797
            else
              E = i(E)
              s = i(s)
              Y = i(Y)
              B = 9502426
              S = nil
              F = i(F)
              A = i(A)
              r = i(r)
            end
          elseif B < 9228883 then
            if B < 8864081 then
              C = T == X
              N = C
              B = 12689286
            else
              B = 4246574
              a = Q[k[2]]
              d = Q[k[3]]
              l = a == d
              I = l
            end
          elseif B < 9273750 then
            B = true
            B = 7854958
          else
            B = 6530184
          end
        elseif B < 13139652 then
          if B < 11480609 then
            if B < 10392540 then
              if B < 9667626 then
                if B < 9590542 then
                  if B < 9501993 then
                    C = Q[a]
                    B = C and 8230290 or 12689286
                    N = C
                  else
                    N = N + q
                    I = C >= N
                    r = not h
                    I = r and I
                    r = C <= N
                    r = h and r
                    I = r or I
                    r = 984263
                    B = I and r
                    I = 9488660
                    B = B or I
                  end
                else
                  Q[a] = R
                  e = 1
                  x = Q[s]
                  D = x + e
                  w = S[D]
                  U = T + w
                  w = 256
                  B = U % w
                  T = B
                  D = Q[A]
                  B = 7998078
                  w = X + D
                  D = 256
                  U = w % D
                  X = U
                end
              elseif B < 10000345 then
                I = 3594582
                d = 10267190
                a = y(-31426)
                l = a ^ d
                B = I - l
                l = B
                I = y(-31446)
                B = I / l
                I = {B}
                B = K[y(-31450)]
              else
                B = 4870978
              end
            elseif B < 10897787 then
              if B < 10602320 then
                B = 12925441
              else
                G = y(-31429)
                X = K[G]
                G = y(-31424)
                T = X[G]
                n = T
                B = 7965424
              end
            elseif B < 11261933 then
              I = y(-31447)
              B = K[I]
              o = y(-31431)
              n = f(1328855, {})
              l = Q[k[4]]
              H = y(-31420)
              d = K[o]
              O = K[H]
              H = {
                O(n)
              }
              O = 2
              P = {
                c(H)
              }
              t = P[O]
              o = d(t)
              d = y(-31442)
              a = l(o, d)
              l = {
                a()
              }
              I = B(c(l))
              a = Q[k[5]]
              l = I
              I = a
              B = a and 13168675 or 13648307
            else
              X = y(-31429)
              P = I
              O = y(-31465)
              I = K[O]
              O = y(-31464)
              B = I[O]
              O = Z()
              H = y(-31429)
              Q[O] = B
              I = K[H]
              H = y(-31433)
              B = I[H]
              T = K[X]
              M = B
              H = B
              B = T and 10880167 or 7965424
              n = T
            end
          elseif B < 12434944 then
            if B < 11755443 then
              if B < 11635581 then
                if B < 11588838 then
                  U = B
                  x = 1
                  D = S[x]
                  x = false
                  w = D == x
                  R = w
                  B = w and 7443034 or 1144440
                else
                  B = 13138638
                  b = 1
                  A = 1
                  h = #G
                  V = d(b, h)
                  b = P(G, V)
                  V = nil
                  h = Q[X]
                  E = b - A
                  r = O(E)
                  h[b] = r
                  b = nil
                end
              else
                B = 1007276
                P = nil
                O = nil
                o = nil
              end
            elseif B < 12093127 then
              a = Q[k[3]]
              d = 247
              l = a * d
              a = 257
              I = l % a
              Q[k[3]] = I
              B = 12211721
            else
              d = 1
              a = Q[k[3]]
              l = a ~= d
              B = l and 16287364 or 11883878
            end
          elseif B < 13005550 then
            if B < 12758835 then
              Q[a] = N
              B = Q[a]
              B = B and 9310308 or 9243409
            else
              B = true
              B = B and 7455894 or 6026729
            end
          elseif B < 13093002 then
            V = b
            A = V
            G[V] = A
            V = nil
            B = 14113674
          else
            b = #G
            h = 0
            V = b == h
            B = V and 110409 or 11634735
          end
        elseif B < 14746779 then
          if B < 13699214 then
            if B < 13540983 then
              if B < 13301702 then
                if B < 13237091 then
                  B = 13648307
                  d = Q[k[6]]
                  a = d == l
                  I = a
                else
                  I = y(-31444)
                  B = K[I]
                  l = y(-31445)
                  I = K[l]
                  l = y(-31445)
                  K[l] = B
                  l = y(-31444)
                  K[l] = I
                  l = Q[k[1]]
                  B = 4870978
                  a = l()
                end
              else
                l = y(-31452)
                d = 0
                B = K[l]
                a = Q[k[8]]
                l = B(a, d)
                B = 1013119
              end
            elseif B < 13658330 then
              l = nil
              Q[k[5]] = I
              B = 1601068
            else
              M = y(-31424)
              B = 14610855
              n = K[M]
              I = n
            end
          elseif B < 14124323 then
            if B < 13901548 then
              P = Q[t]
              I = P
              B = 11419552
            else
              A = not E
              b = b + r
              V = h >= b
              V = A and V
              A = h <= b
              A = E and A
              V = A or V
              A = 13010025
              B = V and A
              V = 1205760
              B = B or V
            end
          elseif B < 14448510 then
            d = y(-31429)
            a = K[d]
            d = y(-31456)
            l = a[d]
            d = Q[k[1]]
            B = K[y(-31438)]
            a = {
              l(d)
            }
            I = {
              c(a)
            }
          else
            M = 3
            n = Z()
            V = W(9880839, {})
            T = 65
            Q[n] = I
            B = Q[O]
            I = B(M, T)
            M = Z()
            G = y(-31420)
            Q[M] = I
            I = K[G]
            B = 0
            T = B
            B = 0
            G = {
              I(V)
            }
            X = B
            B = {
              c(G)
            }
            I = 2
            q = y(-31431)
            G = B
            B = G[I]
            I = y(-31447)
            V = B
            B = K[I]
            b = Q[d]
            C = K[q]
            q = C(V)
            C = y(-31442)
            N = b(q, C)
            b = {
              N()
            }
            I = B(c(b))
            b = Z()
            Q[b] = I
            N = Q[M]
            C = N
            I = 1
            B = 9502426
            N = 1
            q = N
            N = 0
            h = q < N
            N = I - q
          end
        elseif B < 15409788 then
          if B < 15190622 then
            if B < 15070616 then
              if B < 14990471 then
                B = 12925441
              else
                h = y(-31444)
                B = K[h]
                h = y(-31445)
                K[h] = B
                B = 10446202
              end
            else
              H = M
              q = y(-31460)
              C = K[q]
              q = y(-31432)
              N = C[q]
              C = N(l, H)
              N = Q[k[6]]
              q = N()
              b = C + q
              V = b + P
              q = 1
              b = 256
              H = nil
              G = V % b
              b = d[a]
              P = G
              C = P + q
              N = o[C]
              B = 5165514
              V = b .. N
              d[a] = V
            end
          elseif B < 15403159 then
            B = Q[k[1]]
            l = u[1]
            d = B
            a = u[2]
            B = d[a]
            B = B and 15406028 or 971653
          else
            B = 1007276
          end
        elseif B < 16287520 then
          if B < 15774304 then
            B = true
            B = B and 14885354 or 7854958
          else
            T = 13
            a = Q[k[3]]
            d = 32
            n = 2
            l = a % d
            o = Q[k[4]]
            O = Q[k[2]]
            V = Q[k[3]]
            G = V - l
            V = 32
            X = G / V
            M = T - X
            H = n ^ M
            P = O / H
            t = o(P)
            o = 4294967296
            d = t % o
            H = 1
            t = 2
            o = t ^ l
            a = d / o
            o = Q[k[4]]
            T = 256
            O = a % H
            H = 4294967296
            P = O * H
            t = o(P)
            o = Q[k[4]]
            O = 65536
            P = o(a)
            d = t + P
            B = 14152006
            t = 65536
            o = d % t
            n = 256
            P = d - o
            t = P / O
            O = 256
            P = o % O
            l = nil
            H = o - P
            a = nil
            O = H / n
            d = nil
            n = 256
            H = t % n
            M = t - H
            n = M / T
            t = nil
            M = {
              P,
              O,
              H,
              n
            }
            n = nil
            H = nil
            O = nil
            Q[k[1]] = M
            P = nil
            o = nil
          end
        elseif B < 16300060 then
          w = 1
          B = 9659093
          U = S[w]
          R = U
        else
          B = true
          I = {}
          Q[k[1]] = B
          B = K[y(-31455)]
        end
      end
      B = #g
      return c(I)
    end, function(K)
      local y, B = 1, K[1]
      while B do
        l[B], y = l[B] - 1, 1 + y
        if 0 == l[B] then
          l[B], Q[B] = nil, nil
        end
        B = K[y]
      end
    end, function(K, y)
      local c = d(y)
      local function u(u, k)
        return B(K, {u, k}, y, c)
      end
      return u
    end, function(K, y)
      local c = d(y)
      local function u(u, k, g, v, I)
        return B(K, {
          u,
          k,
          g,
          v,
          I
        }, y, c)
      end
      return u
    end, function(K, y)
      local c = d(y)
      local function u(u)
        return B(K, {u}, y, c)
      end
      return u
    end, function(K, y)
      local c = d(y)
      local function u(u, k, g)
        return B(K, {
          u,
          k,
          g
        }, y, c)
      end
      return u
    end, function(K, y)
      local c = d(y)
      local function u(u, k, g, v)
        return B(K, {
          u,
          k,
          g,
          v
        }, y, c)
      end
      return u
    end, 0, function(K, y)
      local c = d(y)
      local function u(...)
        return B(K, {
          ...
        }, y, c)
      end
      return u
    end, {}, function(K, y)
      local c = d(y)
      local function u()
        return B(K, {}, y, c)
      end
      return u
    end, function()
      a = a + 1
      l[a] = 1
      return a
    end
    return t(6675297, {})(c(I))
  end)(getfenv and getfenv() or _ENV, unpack or table[y(-31424)], newproxy, setmetatable, getmetatable, select, {
    ...
  })
end)(...)
