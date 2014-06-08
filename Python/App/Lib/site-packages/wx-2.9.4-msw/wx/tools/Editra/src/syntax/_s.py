###############################################################################
# Name: s.py                                                                  #
# Purpose: Define S and R syntax for highlighting and other features          #
# Author: Cody Precord <cprecord@editra.org>                                  #
# Copyright: (c) 2007 Cody Precord <staff@editra.org>                         #
# License: wxWindows License                                                  #
###############################################################################

"""
FILE: s.py
AUTHOR: Cody Precord
@summary: Lexer configuration module for the S and R statistical languages

"""

__author__ = "Cody Precord <cprecord@editra.org>"
__svnid__ = "$Id: _s.py 70466 2012-01-26 20:55:16Z CJP $"
__revision__ = "$Revision: 70466 $"

#-----------------------------------------------------------------------------#
# Imports
from pygments.token import Token
from pygments.lexers import get_lexer_by_name
import wx
import wx.stc as stc

#Local Imports
import synglob
import syndata

#-----------------------------------------------------------------------------#
# Style Id's

STC_S_DEFAULT, \
STC_S_COMMENT, \
STC_S_NUMBER, \
STC_S_STRING, \
STC_S_STRINGEOL, \
STC_S_OPERATOR, \
STC_S_KEYWORD = range(7)

#-----------------------------------------------------------------------------#

#---- Keyword Specifications ----#

KEYWORDS = ("all array break call else exp for function if length library list "
            "match max mean min while return try NULL NA TRUE FALSE")

R_KEYWORDS = "if else repeat while function for in next break TRUE FALSE NULL NA Inf NaN"
R_KEYWORDS2 = ("abbreviate abline abs acf acos acosh addmargins aggregate agrep "
             "alarm alias alist all anova any aov aperm append apply approx "
             "approxfun apropos ar args arima array arrows asin asinh assign "
             "assocplot atan atanh attach attr attributes autoload autoloader "
             "ave axis backsolve barplot basename beta bindtextdomain binomial "
             "biplot bitmap bmp body box boxplot bquote break browser builtins "
             "bxp by bzfile c call cancor capabilities casefold cat category "
             "cbind ccf ceiling character charmatch chartr chol choose chull "
             "citation class close cm cmdscale codes coef coefficients col "
             "colnames colors colorspaces colours comment complex confint "
             "conflicts contour contrasts contributors convolve cophenetic "
             "coplot cor cos cosh cov covratio cpgram crossprod cummax cummin "
             "cumprod cumsum curve cut cutree cycle data dataentry date dbeta "
             "dbinom dcauchy dchisq de debug debugger decompose delay deltat "
             "demo dendrapply density deparse deriv det detach determinant "
             "deviance dexp df dfbeta dfbetas dffits dgamma dgeom dget dhyper "
             "diag diff diffinv difftime digamma dim dimnames dir dirname "
             "dist dlnorm dlogis dmultinom dnbinom dnorm dotchart double "
             "dpois dput drop dsignrank dt dump dunif duplicated dweibull "
             "dwilcox eapply ecdf edit effects eigen emacs embed end "
             "environment eval evalq example exists exp expression factanal "
             "factor factorial family fft fifo file filter find fitted fivenum "
             "fix floor flush for force formals format formula forwardsolve "
             "fourfoldplot frame frequency ftable function gamma gaussian gc "
             "gcinfo gctorture get getenv geterrmessage gettext gettextf getwd "
             "gl glm globalenv gray grep grey grid gsub gzcon gzfile hat "
             "hatvalues hcl hclust head heatmap help hist history hsv "
             "httpclient iconv iconvlist identical identify if ifelse image "
             "influence inherits integer integrate interaction interactive "
             "intersect invisible isoreg jitter jpeg julian kappa kernapply "
             "kernel kmeans knots kronecker ksmooth labels lag lapply layout "
             "lbeta lchoose lcm legend length letters levels lfactorial "
             "lgamma library licence license line lines list lm load "
             "loadhistory loadings local locator loess log logb logical "
             "loglin lowess ls lsfit machine mad mahalanobis makepredictcall "
             "manova mapply match matlines matplot matpoints matrix max mean "
             "median medpolish menu merge message methods mget min missing "
             "mode monthplot months mosaicplot mtext mvfft names napredict "
             "naprint naresid nargs nchar ncol next nextn ngettext nlevels nlm "
             "nls noquote nrow numeric objects offset open optim optimise "
             "optimize options order ordered outer pacf page pairlist pairs "
             "palette par parse paste pbeta pbinom pbirthday pcauchy pchisq "
             "pdf pentagamma person persp pexp pf pgamma pgeom phyper pi pico "
             "pictex pie piechart pipe plclust plnorm plogis plot pmatch pmax "
             "pmin pnbinom png pnorm points poisson poly polygon polym "
             "polyroot postscript power ppoints ppois ppr prcomp predict "
             "preplot pretty princomp print prmatrix prod profile profiler "
             "proj promax prompt provide psigamma psignrank pt ptukey punif "
             "pweibull pwilcox q qbeta qbinom qbirthday qcauchy qchisq qexp qf "
             "qgamma qgeom qhyper qlnorm qlogis qnbinom qnorm qpois qqline "
             "qqnorm qqplot qr qsignrank qt qtukey quantile quarters quasi "
             "quasibinomial quasipoisson quit qunif quote qweibull qwilcox "
             "rainbow range rank raw rbeta rbind rbinom rcauchy rchisq "
             "readline real recover rect reformulate regexpr relevel remove "
             "reorder rep repeat replace replicate replications require "
             "reshape resid residuals restart return rev rexp rf rgamma rgb "
             "rgeom rhyper rle rlnorm rlogis rm rmultinom rnbinom rnorm round "
             "row rownames rowsum rpois rsignrank rstandard rstudent rt rug "
             "runif runmed rweibull rwilcox sample sapply save savehistory "
             "scale scan screen screeplot sd search searchpaths seek segments "
             "seq sequence serialize setdiff setequal setwd shell sign signif "
             "sin single sinh sink smooth solve sort source spectrum spline "
             "splinefun split sprintf sqrt stack stars start stderr stdin "
             "stdout stem step stepfun stl stop stopifnot str strftime "
             "strheight stripchart strptime strsplit strtrim structure "
             "strwidth strwrap sub subset substitute substr substring sum "
             "summary sunflowerplot supsmu svd sweep switch symbols symnum "
             "system t table tabulate tail tan tanh tapply tempdir tempfile "
             "termplot terms tetragamma text time title toeplitz tolower "
             "topenv toupper trace traceback transform trigamma trunc truncate "
             "try ts tsdiag tsp typeof unclass undebug union unique uniroot "
             "unix unlink unlist unname unserialize unsplit unstack untrace "
             "unz update upgrade url var varimax vcov vector version vi "
             "vignette warning warnings weekdays weights which while window "
             "windows with write wsbrowser xedit xemacs xfig xinch xor xtabs "
             "xyinch yinch zapsmall")
R_KEYWORDS3 = ("acme aids aircondit amis aml banking barchart barley beaver "
                "bigcity boot brambles breslow bs bwplot calcium cane "
                "capability cav censboot channing city claridge cloth cloud "
                "coal condense contourplot control corr darwin densityplot "
                "dogs dotplot ducks empinf envelope environmental ethanol fir "
                "frets gpar grav gravity grob hirose histogram islay knn "
                "larrows levelplot llines logit lpoints lsegments lset ltext "
                "lvqinit lvqtest manaus melanoma melanoma motor multiedit "
                "neuro nitrofen nodal ns nuclear oneway parallel paulsen "
                "poisons polar qq qqmath remission rfs saddle salinity shingle "
                "simplex singer somgrid splom stripplot survival tau tmd "
                "tsboot tuna unit urine viewport wireframe wool xyplot")

#---- Syntax Style Specs ----#
if wx.VERSION >= (2, 9, 0, 0, ''):
    SYNTAX_ITEMS = [ (stc.STC_R_BASEKWORD,  'class_style'), #TODO
                     (stc.STC_R_COMMENT,    'comment_style'),
                     (stc.STC_R_DEFAULT,    'default_style'),
                     (stc.STC_R_IDENTIFIER, 'default_style'),
                     (stc.STC_R_INFIX,      'default_style'), #TODO
                     (stc.STC_R_INFIXEOL,   'default_style'), #TODO
                     (stc.STC_R_KWORD,      'keyword_style'),
                     (stc.STC_R_NUMBER,     'number_style'),
                     (stc.STC_R_OPERATOR,   'operator_style'),
                     (stc.STC_R_OTHERKWORD, 'keyword2_style'),
                     (stc.STC_R_STRING,     'string_style'),
                     (stc.STC_R_STRING2,    'char_style')] #TODO
else:
    SYNTAX_ITEMS = [ (STC_S_DEFAULT,   'default_style'),
                     (STC_S_COMMENT,   'comment_style'),
                     (STC_S_NUMBER,    'number_style'),
                     (STC_S_STRING,    'string_style'),
                     (STC_S_STRINGEOL, 'stringeol_style'),
                     (STC_S_OPERATOR,  'operator_style'),
                     (STC_S_KEYWORD,   'keyword_style') ]

#-----------------------------------------------------------------------------#

class SyntaxData(syndata.SyntaxDataBase):
    """SyntaxData object for R and S""" 
    def __init__(self, langid):
        super(SyntaxData, self).__init__(langid)

        # Setup
        if wx.VERSION >= (2, 9, 0, 0, ''):
            self.SetLexer(stc.STC_LEX_R)
        else:
            self.SetLexer(stc.STC_LEX_CONTAINER)
            self.RegisterFeature(synglob.FEATURE_STYLETEXT, StyleText)

    def GetKeywords(self):
        """Returns Specified Keywords List """
        if wx.VERSION >= (2, 9, 0, 0, ''):
            return [(0, R_KEYWORDS), (1, R_KEYWORDS2), (2, R_KEYWORDS3)]
        else:
            return [(1, KEYWORDS)]

    def GetSyntaxSpec(self):
        """Syntax Specifications """
        return SYNTAX_ITEMS

    def GetCommentPattern(self):
        """Returns a list of characters used to comment a block of code """
        return [u"#",]

#-----------------------------------------------------------------------------#

def StyleText(_stc, start, end):
    """Style the text
    @param _stc: Styled text control instance
    @param start: Start position
    @param end: end position
    @todo: performance improvements
    @todo: style errors caused by unicode characters (related to internal utf8)

    """
    cpos = 0
    _stc.StartStyling(cpos, 0x1f)
    lexer = get_lexer_by_name("s")
    is_wineol = _stc.GetEOLMode() == stc.STC_EOL_CRLF
    for token, txt in lexer.get_tokens(_stc.GetTextRange(0, end)):
        style = TOKEN_MAP.get(token, STC_S_DEFAULT)

        tlen = len(txt)

        # Account for \r\n end of line characters
        if is_wineol and "\n" in txt:
            tlen += txt.count("\n")

        if tlen:
            _stc.SetStyling(tlen, style)
        cpos += tlen
        _stc.StartStyling(cpos, 0x1f)

#-----------------------------------------------------------------------------#

TOKEN_MAP = { Token.Literal.String  : STC_S_STRING,
              Token.Comment         : STC_S_COMMENT,
              Token.Comment.Single  : STC_S_COMMENT,
              Token.Operator        : STC_S_OPERATOR,
              Token.Punctuation     : STC_S_OPERATOR,
              Token.Number          : STC_S_NUMBER,
              Token.Literal.Number  : STC_S_NUMBER,
              Token.Keyword         : STC_S_KEYWORD,
              Token.Keyword.Constant: STC_S_KEYWORD }
              