#include <math.h>
#include <cairo.h>
#include <gtk/gtk.h>

static void do_drawing(cairo_t *);
void line (cairo_t *cr, double x1, double y1, double x2, double y2);
void grafico(cairo_t *cr);

#define WX  800    // dimensÃµes da janela
#define WY  600

#define CX   120    // centro da tela
#define CY   120

static gboolean on_draw_event(GtkWidget *widget, cairo_t *cr, 
    gpointer user_data)
{      
  do_drawing(cr);

  return FALSE;
}

void line (cairo_t *cr, double x1, double y1, double x2, double y2)
 {
    cairo_move_to (cr, 100*x1 + CX, WY - 100*y1 - CY);
    cairo_line_to (cr, 100*x2 + CX, WY - 100*y2 - CY);
    cairo_stroke(cr);
 }

int cairo_init(int argc, char *argv[])
{
  GtkWidget *window;
  GtkWidget *darea;

  gtk_init(&argc, &argv);

  window = gtk_window_new(GTK_WINDOW_TOPLEVEL);

  darea = gtk_drawing_area_new();
  gtk_container_add(GTK_CONTAINER(window), darea);

  g_signal_connect(G_OBJECT(darea), "draw", 
      G_CALLBACK(on_draw_event), NULL); 
  g_signal_connect(window, "destroy",
      G_CALLBACK(gtk_main_quit), NULL);

  // gtk_window_set_position(GTK_WINDOW(window), GTK_WIN_POS_CENTER);
  gtk_window_set_default_size(GTK_WINDOW(window), WX, WY); 
  gtk_window_set_title(GTK_WINDOW(window), "GTK window");

  gtk_widget_show_all(window);

  gtk_main();

  return 0;
}

static void do_drawing(cairo_t *cr)
{
  cairo_set_source_rgb(cr, 0, 0, 0);
  cairo_rectangle(cr, 0.0, 0.0, WX, WY);
  cairo_fill(cr);

  cairo_set_source_rgb(cr, 1.0, 1.0, 1.0);

  grafico(cr);
}

// ---------------------------------------------------------------------------
//  
// ---------------------------------------------------------------------------

void grafico(cairo_t *cr)
{
   double  x1, y1, x2, y2;

   line (cr, -0.5, 0.0, 6.0, 0.0);      // eixo X
   line (cr, 5.9, -0.1, 6.0, 0.0);
   line (cr, 5.9,  0.1, 6.0, 0.0);

   line (cr, 0.0, -0.5, 0.0, 4.0);      // eixo Y
   line (cr, -0.1, 3.9, 0.0, 4.0);      
   line (cr,  0.1, 3.9, 0.0, 4.0);      

   cairo_set_source_rgb(cr, 1.0, 1.0, 0.0);    //  yellow
   x1 = 0; 
   y1 = x1 * x1 / 7;
   for (x2=0.1;x2<=5;x2+=0.1)
    {
       y2 = x2 * x2 / 7;
       line (cr, x1,y1, x2,y2);
       x1 = x2;   y1 = y2;
    }


   cairo_set_source_rgb(cr, 0.5, 1.0, 0.0);    //  green
   x1 = 0; 
   y1 = ( (x1 - 2) * (x1 -2) * (x1 - 2) + 1)/ 10 + 0.5;
   for (x2=0.1;x2<=5;x2+=0.1)
    {
       y2 = ( (x2 - 2) * (x2 -2) * (x2 - 2) + 1)/ 10 + 0.5;
       line (cr, x1,y1, x2,y2);
       x1 = x2;   y1 = y2;
    }


   cairo_set_source_rgb(cr, 0.5, 0.8, 0.9);    //  blue
   x1 = 0; 
   y1 = x1 * sin(x1*10) / 6;
   for (x2=0.02;x2<=5;x2+=0.02)
    {
       y2 = x2 * sin(x2*10) / 6;
       line (cr, x1,y1, x2,y2);
       x1 = x2;   y1 = y2;
    }

return;
 
   cairo_set_source_rgb(cr, 1.0, 0.3, 0.3);    //  red
   x1 = 0; 
   y1 = log(x1+1);
   for (x2=0.02;x2<=5;x2+=0.02)
    {
       y2 = log(x2+1);
       line (cr, x1,y1, x2,y2);
       x1 = x2;   y1 = y2;
    }
}

int main(int argc, char *argv[])
{
  cairo_init (argc, argv);
}
