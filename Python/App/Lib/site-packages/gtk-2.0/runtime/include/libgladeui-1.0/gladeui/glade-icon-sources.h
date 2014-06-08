/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
/*
 * Copyright (C) 2008 Tristan Van Berkom.
 *
 * This library is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public 
 * License along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 * Authors:
 *   Tristan Van Berkom <tvb@gnome.org>
 */
#ifndef _GLADE_ICON_SOURCES_H_
#define _STV_CAP_H_

#include <glib.h>

G_BEGIN_DECLS

struct _GladeIconSources
{
	GHashTable *sources;

};

typedef struct _GladeIconSources         GladeIconSources;
typedef struct _GladeParamIconSources    GladeParamIconSources;

#define	GLADE_TYPE_ICON_SOURCES       (glade_icon_sources_get_type())
#define GLADE_TYPE_EPROP_ICON_SOURCES (glade_eprop_icon_sources_get_type())

GType             glade_icon_sources_get_type          (void) G_GNUC_CONST;
GType             glade_eprop_icon_sources_get_type    (void) G_GNUC_CONST;

GladeIconSources *glade_icon_sources_new               (void);
GladeIconSources *glade_icon_sources_copy              (GladeIconSources *sources);
void              glade_icon_sources_free              (GladeIconSources *sources);

G_END_DECLS

#endif /* _GLADE_ICON_SOURCE_H_ */
