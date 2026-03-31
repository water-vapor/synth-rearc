from synth_rearc.core import *

from .verifier import verify_97a05b5b


def generate_97a05b5b(diff_lb: float, diff_ub: float) -> dict:
    while True:
        cols = interval(ZERO, TEN, ONE)
        h = unifint(diff_lb, diff_ub, (15, 30))
        w = unifint(diff_lb, diff_ub, (15, 30))
        sgh = randint(h // THREE, (h // THREE) * TWO)
        sgw = randint(w // THREE, (w // THREE) * TWO)
        bgc = ZERO
        sqc = TWO
        remcols = remove(bgc, remove(sqc, cols))
        gi = canvas(bgc, (h, w))
        oh = randint(TWO, sgh // TWO)
        ow = randint(TWO, sgw // TWO)
        nobjs = unifint(diff_lb, diff_ub, (ONE, EIGHT))
        objs = set()
        cands = asindices(canvas(NEG_ONE, (oh, ow)))
        forbidden = set()
        tr = ZERO
        maxtr = FOUR * nobjs
        while len(objs) != nobjs and tr < maxtr:
            tr += ONE
            obj = {choice(totuple(cands))}
            ncells = randint(ONE, oh * ow - ONE)
            for _ in range(ncells - ONE):
                obj.add(choice(totuple((cands - obj) & mapply(neighbors, obj))))
            obj |= choice((dmirror, cmirror, vmirror, hmirror))(obj)
            if len(obj) == height(obj) * width(obj):
                continue
            obj = frozenset(obj)
            objn = normalize(obj)
            if objn not in forbidden:
                objs.add(objn)
            for augmf1 in (identity, dmirror, cmirror, hmirror, vmirror):
                for augmf2 in (identity, dmirror, cmirror, hmirror, vmirror):
                    forbidden.add(augmf1(augmf2(objn)))
        tr = ZERO
        maxtr = FIVE * nobjs
        succ = ZERO
        loci = randint(ZERO, h - sgh)
        locj = randint(ZERO, w - sgw)
        bd = backdrop(frozenset({(loci, locj), (loci + sgh - ONE, locj + sgw - ONE)}))
        gi = fill(gi, sqc, bd)
        go = canvas(sqc, (sgh, sgw))
        goinds = asindices(go)
        giinds = asindices(gi) - shift(goinds, (loci, locj))
        giinds = giinds - mapply(neighbors, shift(goinds, (loci, locj)))
        while succ < nobjs and tr < maxtr and len(objs) > ZERO:
            tr += ONE
            obj = choice(totuple(objs))
            col = choice(remcols)
            subgi = fill(canvas(col, shape(obj)), sqc, obj)
            if len(palette(subgi)) == ONE:
                continue
            f1 = choice((identity, dmirror, vmirror, cmirror, hmirror))
            f2 = choice((identity, dmirror, vmirror, cmirror, hmirror))
            f = compose(f1, f2)
            subgo = f(subgi)
            giobj = asobject(subgi)
            goobj = asobject(subgo)
            ohi, owi = shape(giobj)
            oho, owo = shape(goobj)
            gocands = sfilter(goinds, lambda ij: ij[ZERO] <= sgh - oho and ij[ONE] <= sgw - owo)
            if len(gocands) == ZERO:
                continue
            goloc = choice(totuple(gocands))
            goplcd = shift(goobj, goloc)
            goplcdi = toindices(goplcd)
            if not goplcdi.issubset(goinds):
                continue
            gicands = sfilter(giinds, lambda ij: ij[ZERO] <= h - ohi and ij[ONE] <= w - owi)
            if len(gicands) == ZERO:
                continue
            giloc = choice(totuple(gicands))
            giplcd = shift(giobj, giloc)
            giplcdi = toindices(giplcd)
            if not giplcdi.issubset(giinds):
                continue
            succ += ONE
            remcols = remove(col, remcols)
            objs = remove(obj, objs)
            goinds = goinds - goplcdi
            giinds = (giinds - giplcdi) - mapply(neighbors, giplcdi)
            gi = paint(gi, giplcd)
            gi = fill(gi, bgc, sfilter(shift(goplcd, (loci, locj)), lambda cij: cij[ZERO] == sqc))
            go = paint(go, goplcd)
        try:
            x0 = verify_97a05b5b(gi)
        except Exception:
            continue
        if x0 != go:
            continue
        if ZERO not in palette(gi) or TWO not in palette(gi):
            continue
        if ZERO in palette(go) or TWO not in palette(go):
            continue
        return {"input": gi, "output": go}
