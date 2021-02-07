#!/usr/bin/env python

from numpy import *

def pageRankGenerator(At = [array((), int64)],   numLinks = array((), int64),   ln = array((), int64), alpha = 0.85,  convergence = 0.0001,  checkSteps = 10 ):

    # the number of "pages"
    N = len(At)

    # the number of "pages without links"
    M = ln.shape[0]

    # initialize: single-precision should be good enough
    iNew = ones((N,), float64) / N
    iOld = ones((N,), float64) / N

    done = False
    while not done:

        # normalize every now and then for numerical stability
        iNew /= sum(iNew)

        for step in range(checkSteps):

            # swap arrays
            iOld, iNew = iNew, iOld

            # an element in the 1 x I vector. 
            # all elements are identical.
            oneIv = (1 - alpha) * sum(iOld) / N

            # an element of the A x I vector.
            # all elements are identical.
            oneAv = 0.0
            if M > 0:
                oneAv = alpha * sum(iOld.take(ln, axis = 0)) / N

            # the elements of the H x I multiplication
            ii = 0 
            while ii < N:
                page = At[ii]
                h = 0
                if page.shape[0]:
                    h = alpha * dot(
                            iOld.take(page, axis = 0),
                            1. / numLinks.take(page, axis = 0)
                            )
                iNew[ii] = h + oneAv + oneIv
                ii += 1

        diff = sum(abs(iNew - iOld))
        done = (diff < convergence)

        yield iNew


def transposeLinkMatrix(  outGoingLinks = [[]]):

    nPages = len(outGoingLinks)
    # incomingLinks[ii] will contain the indices jj of the pages
    # linking to page ii
    incomingLinks = [[] for ii in range(nPages)]
    # the number of links in each page
    numLinks = zeros(nPages, int64)
    # the indices of the leaf nodes
    leafNodes = []

    for ii in range(nPages):
        if len(outGoingLinks[ii]) == 0:
            leafNodes.append(ii)
        else:
            numLinks[ii] = len(outGoingLinks[ii])
            # transpose the link matrix
            for jj in outGoingLinks[ii]:
                incomingLinks[jj].append(ii)

    incomingLinks = [array(ii) for ii in incomingLinks]
    numLinks = array(numLinks)
    leafNodes = array(leafNodes)

    return incomingLinks, numLinks, leafNodes


def pageRank(linkMatrix = [[]],  alpha = 0.85,  convergence = 0.0001,  checkSteps = 10 ):

    incomingLinks, numLinks, leafNodes = transposeLinkMatrix(linkMatrix)

    for gr in pageRankGenerator(incomingLinks, numLinks, leafNodes,alpha = alpha, convergence = convergence, checkSteps = checkSteps):
        final = gr

    return final
