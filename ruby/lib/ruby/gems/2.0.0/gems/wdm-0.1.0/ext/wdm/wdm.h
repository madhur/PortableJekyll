#include <stdio.h>

#define WINVER 0x0500       // Support Windows 2000 and later,
#define _WIN32_WINNT 0x0500 // this is needed for 'GetLongPathNameW'

#ifndef VC_EXTRALEAN
#define VC_EXTRALEAN        // Exclude rarely-used stuff from Windows headers
#endif

#include <Windows.h>

#include <ruby.h>
#include <ruby/encoding.h>

#ifndef WDM_H
#define WDM_H

#ifdef __cplusplus
extern "C" {
#endif // __cplusplus

// ---------------------------------------------------------
// Constants
// ---------------------------------------------------------

#define WDM_DEBUG_ENABLED FALSE

#define WDM_BUFFER_SIZE 16384 // 2^14 or 16Kb

// The maximum WCHAR's for buffers used in functions that have
// a unicode variant and require to prepend "\\?\" to the path
#define WDM_MAX_WCHAR_LONG_PATH 32767

// ---------------------------------------------------------
// Macros
// ---------------------------------------------------------

#if WDM_DEBUG_ENABLED == TRUE
    #define WDM_DEBUG(str, ...) \
        fprintf(stderr, "[DEBUG] (%s@%d): " str "\n", __FILE__, __LINE__, ##__VA_ARGS__)

    #define WDM_WDEBUG(str, ...) \
        fwprintf(stderr, L"[DEBUG] (%S@%d): " str "\n", __FILE__, __LINE__, ##__VA_ARGS__)

#else
    #define WDM_DEBUG(str, ...)
    #define WDM_WDEBUG(str, ...)
#endif

// ----------------------------------------------------------
// Extern global variables
// ----------------------------------------------------------

extern VALUE mWDM;

extern VALUE eWDM_Error;

extern rb_encoding *wdm_rb_enc_utf8;

// ---------------------------------------------------------
// Prototypes
// ---------------------------------------------------------

void Init_wdm_ext();

// ---------------------------------------------------------

#ifdef __cplusplus
}
#endif // __cplusplus

#endif // WDM_H